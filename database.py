import csv
import random
import sys
from signal import SIGINT, signal
from threading import Thread
from time import sleep

from paho.mqtt import client as mqtt_client

broker = '192.168.1.10'
port = 1883
topic = "em/lane_2"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

ambulance = "em/lanes"
mqtt_emergency = "em/emergency"
mqtt_lane_1 = "em/lane_1"
mqtt_lane_2 = "em/lane_2"
mqtt_lane_3 = "em/lane_3"
mqtt_lane_4 = "em/lane_4"
siren = "em/sound"
thread = True

client = None
lane = 0
sound = 0
emergency = 0
lane_1 = 0
lane_2 = 0
lane_3 = 0
lane_4 = 0


def main():
    global lane, sound, client
    count = 0

    signal(SIGINT, handle_sigint)
    thread = Thread(target=task)
    thread.start()
    # print('Connected')
    sleep(2)
    print('LISTENING')
    with open('dataset.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Sound", "Lane 1", "Lane 2", "Lane 3",
                        "Lane 4", "Emergency Status", "Emergency Lane"])
        while True:
            print('Writing...')
            writer.writerow(
                [sound, lane_1, lane_2, lane_3, lane_4, lane, emergency])
            sleep(1)


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


def publish(client, s_topic, text):
    msg = f"{text}"
    result = client.publish(s_topic, msg)
    status = result[0]


def subscribe(client: mqtt_client, s_topic):
    def on_message(client, userdata, msg):
        global lane, sound, lane_1, lane_2, lane_3, lane_4, emergency
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if msg.topic == 'em/lanes':
            lane = msg.payload.decode()
        elif msg.topic == 'em/sound':
            sound = msg.payload.decode()
        elif msg.topic == 'em/lane_1':
            lane_1 = msg.payload.decode()
        elif msg.topic == 'em/lane_2':
            lane_2 = msg.payload.decode()
        elif msg.topic == 'em/lane_3':
            lane_3 = msg.payload.decode()
        elif msg.topic == 'em/lane_4':
            lane_4 = msg.payload.decode()
        elif msg.topic == 'em/emergency':
            emergency = msg.payload.decode()

    client.subscribe(s_topic)
    client.on_message = on_message


def handle_sigint(signalum, frame):
    sys.exit()


def task():
    print('Subsribe Thread Starting')
    try:
        global client
        client = connect_mqtt()
        subscribe(client, ambulance)
        subscribe(client, mqtt_emergency)
        subscribe(client, mqtt_lane_2)
        subscribe(client, mqtt_lane_1)
        subscribe(client, mqtt_lane_3)
        subscribe(client, mqtt_lane_4)
        subscribe(client, siren)
        client.loop_start()
    except KeyboardInterrupt:
        client.loop_stop()


if __name__ == '__main__':
    main()
