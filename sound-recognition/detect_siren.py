import random
from queue import Queue
from time import sleep

import numpy as np
import pandas as pd
import soundcard as sc
import torch
from audioclassifier import AudioClassifier
from audiomanipulation import AudioUtil
from paho.mqtt import client as mqtt_client
from torchaudio import transforms

auds = []
win = 3
count = 0

topic = "em/sound"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
broker = 'localhost'
port = 1883


def open_file(audio_file, sr):
    return (audio_file, sr)


# Check if gpu is available
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Import Trained model
trained_model = AudioClassifier()
trained_model.load_state_dict(torch.load(
    'D://Thesis//Emergency Priority//sound-recognition//siren_detection_model_4.pth'))
trained_model = trained_model.to(device)
trained_model.eval()

mics = sc.all_microphones()
speaker = sc.get_speaker('Realtek')
usb_microphone = sc.default_microphone()
print("Microphone Selected:", usb_microphone)


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, text, tp):
    msg = f"{text}"
    result = client.publish(tp, msg)
    # result: [0, 1]
    status = result[0]


def detect_ambulance():

    duration = 3000
    new_sr = 44100
    shift_pct = 0.4
    n_mels = 64
    n_fft = 1024
    hop_len = None
    top_db = 80
    channel = 2
    sr = 44100
    init = False

    with usb_microphone.recorder(samplerate=44100) as mic, \
            speaker.player(samplerate=44100) as sp:
        batch = 0
        frames = []
        waves = []
        print("Recording...")
        try:
            while True:
                data = mic.record(numframes=2000)
                # print(data.shape)
                frames.append(data)
                # print(len(frames))

                if batch >= 2:
                    #print(batch)
                    stacked = np.stack(waves)
                    final_audio = torch.tensor(stacked)

                    print('-----DETECTING FROM BATCH-----')

                    # batch_q.put(final_audio)
                    direct_inference(trained_model, client, final_audio)

                    batch = 0
                    waves = []

                if len(frames) > (new_sr * 3) / 1024 and not init:
                    print('Initial')
                    aud = np.stack(frames)
                    # merge to 2D 3sec windows
                    aud = aud.transpose(2, 0, 1).reshape(2, -1)

                    # convert to tensor
                    tensor_mic = torch.tensor(aud)
                    tensor_mic = tensor_mic.float()

                    aud = open_file(tensor_mic, sr)

                    reaud = AudioUtil.resample(aud, new_sr)
                    rechan = AudioUtil.rechannel(reaud, channel)

                    dur_aud = AudioUtil.pad_trunc(rechan, duration)
                    shift_aud = AudioUtil.time_shift(dur_aud, shift_pct)
                    sgram = AudioUtil.spectro_gram(
                        shift_aud, n_mels=64, n_fft=1024, hop_len=None)
                    # aug_sgram = AudioUtil.spectro_augment(sgram, max_mask_pct=0.1, n_freq_masks=2, n_time_masks=2)

                    waves.append(sgram.numpy())
                    batch += 1
                    init = True

                if init and len(frames) > 160:
                    # print('frames: ', len(frames))
                    frames = frames[30:]
                    aud = np.stack(frames)
                    # merge to 2D 3sec windows
                    aud = aud.transpose(2, 0, 1).reshape(2, -1)

                    # convert to tensor
                    tensor_mic = torch.tensor(aud)
                    tensor_mic = tensor_mic.float()

                    aud = open_file(tensor_mic, sr)

                    reaud = AudioUtil.resample(aud, new_sr)
                    rechan = AudioUtil.rechannel(reaud, channel)

                    dur_aud = AudioUtil.pad_trunc(rechan, duration)
                    shift_aud = AudioUtil.time_shift(dur_aud, shift_pct)
                    sgram = AudioUtil.spectro_gram(
                        shift_aud, n_mels=64, n_fft=1024, hop_len=None)
                    # aug_sgram = AudioUtil.spectro_augment(sgram, max_mask_pct=0.1, n_freq_masks=2, n_time_masks=2)

                    # plot_spectrogram(sgram[0], new_sr)
                    waves.append(sgram.numpy())

                    batch += 1
        except KeyboardInterrupt:
            print('Detection Stopped')
            client.disconnect()


def direct_inference(model, client, audio):
    detect = 0
    not_detect = 0
    batch = 0

    print('Fetching')
    data = audio
    is_ambulance = False
    # for i in range(2):
    # plot_spectrogram(data[i][0], 44100)

    # Disable gradient updates
    with torch.no_grad():
        # Get the input features and target labels, and put them on the GPU
        inputs = data.to(device)

        # Normalize the inputs
        inputs_m, inputs_s = inputs.float().mean(), inputs.std()
        input = (inputs - inputs_m) / inputs_s

        outputs = model(input)

        # Get the predicted class with the highest score
        probs = torch.nn.functional.softmax(outputs, dim=1)
        conf, prediction = torch.max(probs, 1)

        common_conf = (conf[0] + conf[1])/2

        print(prediction[0], conf[0])
        print(prediction[1], conf[1])
        print(common_conf)

        if prediction[0] == 1 and prediction[1] == 1 and common_conf > 0.80:
            is_ambulance = True
        elif prediction[0] == 1 or prediction[1] == 1:
            # print(conf)
            if common_conf > 0.60:
                is_ambulance = True

        # clear_output()
        if is_ambulance:
            print('SIREN PRESENT', common_conf)
            publish(client, 1, topic)

        else:
            print('NO SIREN PRESENT')
            publish(client, 0, topic)


client = connect_mqtt()

record_state = Queue()
batch_q = Queue()

record_state.put(True)

print('Starting Siren Detection on', device)
detect_ambulance()
