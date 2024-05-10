import random
import sys
from signal import SIGINT, signal
from threading import Thread
from time import sleep

from paho.mqtt import client as mqtt_client

broker = '192.168.1.18'
port = 1883
topic = "em/lane_2"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

ambulance = "em/lanes"
mqtt_lane_1 = "em/lane_1"
mqtt_lane_2 = "em/lane_2"
mqtt_lane_3 = "em/lane_3"
mqtt_lane_4 = "em/lane_4"
siren = "em/sound"
thread = True

client = None
lane = 0
sound = 0
lane_1 = 0
lane_2 = 0
lane_3 = 0
lane_4 = 0


def main():
    val = [0, 0]
    temp = [0, 0]
    first = 0
    emergency_status = False
    emergency_lane = 0
    # temp = True
    global lane, sound, client

    signal(SIGINT, handle_sigint)
    thread = Thread(target=task)
    thread.start()
    # print('Connected')
    sleep(2)
    print('LISTENING')
    while True:
        # publish(client, 'em/emergency', 'NO EMERGENCY')
        if int(sound) == 0:
            if emergency_status:
                emergency_status = False

        if int(lane_1) == 0:
            if emergency_status:
                emergency_status = False
        elif int(lane_2) == 0:
            if emergency_status:
                emergency_status = False
        elif int(lane_3) == 0:
            if emergency_status:
                emergency_status = False
        elif int(lane_4) == 0:
            if emergency_status:
                emergency_status = False

        # SIREN FIRST DETECTION
        if int(sound) == 1:
            # print('AMBULANCE SIREN DETECTED')
            if int(lane_1) == 1:
                if not emergency_status:
                    emergency_status = True
                    emergency_lane = 0
            elif int(lane_2) == 1:
                if not emergency_status:
                    emergency_status = True
                    emergency_lane = 1
            elif int(lane_3) == 1:
                if not emergency_status:
                    emergency_status = True
                    emergency_lane = 2
            elif int(lane_4) == 1:
                if not emergency_status:
                    emergency_status = True
                    emergency_lane = 3

        # AMBULANCE FIRST DETECTION
        if int(lane_1) == 1:
            if int(sound) == 1:
                if not emergency_status:
                    emergency_status = True
                    emergency_lane = 0
        elif int(lane_2) == 1:
            if int(sound) == 1:
                if not emergency_status:
                    emergency_status = True
                    emergency_lane = 1
        elif int(lane_3) == 1:
            if int(sound) == 1:
                if not emergency_status:
                    emergency_status = True
                    emergency_lane = 2
        elif int(lane_4) == 1:
            if int(sound) == 1:
                if not emergency_status:
                    emergency_status = True
                    emergency_lane = 3

        if emergency_status:
            if emergency_lane == 0:
                print('-----LANE 1 EMERGENCY-----')
                publish(client, 'em/emergency', 'LANE 1 EMERGENCY')
            elif emergency_lane == 1:
                print('-----LANE 2 EMERGENCY-----')
                publish(client, 'em/emergency', 'LANE 2 EMERGENCY')
            elif emergency_lane == 2:
                print('-----LANE 3 EMERGENCY-----')
                publish(client, 'em/emergency', 'LANE 3 EMERGENCY')
            elif emergency_lane == 3:
                print('-----LANE 4 EMERGENCY-----')
                publish(client, 'em/emergency', 'LANE 4 EMERGENCY')
        else:
            publish(client, 'em/emergency', 'NO EMERGENCY')


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
        global lane, sound, lane_1, lane_2, lane_3, lane_4
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
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
        subscribe(client, mqtt_lane_2)
        subscribe(client, mqtt_lane_1)
        subscribe(client, mqtt_lane_3)
        subscribe(client, mqtt_lane_4)
        subscribe(client, siren)
        client.loop_forever()
    except KeyboardInterrupt:
        client.loop_stop()


if __name__ == '__main__':
    main()
