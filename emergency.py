import random
import sys
from _thread import interrupt_main
from signal import SIGINT, signal
from threading import Thread
from time import sleep

import cv2
import numpy as np
from paho.mqtt import client as mqtt_client

broker = '192.168.1.18'
port = 1883
# topic = "em/lanes"
ambulance = "em/emergency"
mqtt_lane_1 = "em/lane_1"
mqtt_lane_2 = "em/lane_2"
siren = "em/sound"
thread = True

lane = 0
sound = 0
lane_1 = 0
lane_2 = 0
ambulance_emergency = 0

count = 0

trigger = False
values = {}

f = open("ambulance_siren_test.txt", 'a')

client_id = f'python-mqtt-{random.randint(1000, 10000)}'


def main():

    # temp = True
    global lane, sound, trigger, values, count, ambulance_emergency

    signal(SIGINT, handle_sigint)
    thread = Thread(target=task)
    thread.start()
    client = connect_mqtt()
    # print('Connected')
    sleep(5)
    print('LISTENING')
    try:
        while True:
            # subscribe(client, ambulance)
            # subscribe(client, mqtt_lane_2)
            # publish(client)
            count += 1
            temp = []
            temp.append(lane_1)
            temp.append(sound)
            temp.append(ambulance_emergency)

            # print(values.keys())
            if str(temp) in values.keys():
                for i in values.keys():
                    if i == str(temp):
                        values[i] += 1
                        f.write(f'{i}: {values[i]} ---- Frame: {count}\n')
                        # print(i, values[i])
            else:
                # print(f'Added: {str(temp)}')
                print("Added New Sequence")
                values.update({str(temp): 1})
                temp = []

            sleep(0.5)
    except KeyboardInterrupt:
        for i in values.keys():
            print('Appended New Sequence')
            f.write(f'{i}: {values[i]}\n')

        print('Write to file')
        f.close()


def connect_mqtt():

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set('josiah', 'password')
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(mqtt_lane_1, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{mqtt_lane_1}`")
        else:
            print(f"Failed to send message to topic {mqtt_lane_1}")
        msg_count += 1


def subscribe(client: mqtt_client, s_topic):

    def on_message(client, userdata, msg):
        global lane, sound, lane_1, lane_2, ambulance_emergency
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if msg.topic == 'em/lanes':
            lane = int(msg.payload.decode())
        elif msg.topic == 'em/sound':
            sound = int(msg.payload.decode())
        elif msg.topic == 'em/lane_1':
            lane_1 = int(msg.payload.decode())
        elif msg.topic == 'em/lane_2':
            lane_2 = int(msg.payload.decode())
        elif msg.topic == 'em/emergency':
            ambulance_emergency = int(msg.payload.decode())

    client.subscribe(s_topic)
    client.on_message = on_message


def task():
    print('Subsribe Thread Starting')
    global values
    try:
        client = connect_mqtt()
        subscribe(client, ambulance)
        subscribe(client, mqtt_lane_2)
        subscribe(client, mqtt_lane_1)
        subscribe(client, siren)
        print('Subsribe Thread Started')
        client.loop_start()
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()


def handle_sigint(signalum, frame):
    global count
    for i in values.keys():
        print(f'Writing To File: {i}')
        f.write(f'{i}: {values[i]}\n')
    f.write(f'Total Frames: {count}')
    f.write('\n\n')

    print('Write to file')
    f.close()
    sys.exit()


if __name__ == '__main__':
    main()
