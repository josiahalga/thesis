import random
import sys
from signal import SIGINT, signal
from threading import Thread
from time import sleep

from paho.mqtt import client as mqtt_client

broker = '192.168.1.1'
port = 1883
topic = "em/lane_2"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

ambulance = "em/lanes"
mqtt_lane_1 = "em/lane_1"
mqtt_lane_2 = "em/lane_2"
siren = "em/sound"
thread = True

lane = 0
sound = 0
lane_1 = 0
lane_2 = 0


def main():
    val = [0, 0]
    temp = [0, 0]
    first = 0
    change = False
    # temp = True
    global lane, sound, trigger

    signal(SIGINT, handle_sigint)
    thread = Thread(target=task)
    thread.start()
    client = connect_mqtt()
    # print('Connected')
    print('LISTENING')
    while True:

        if int(lane_1) == 1 and int(sound) == 1:
            print('----LANE 1 EMERGENCY----')
            first = 0
        elif int(lane_2) == 1 and int(sound) == 1:
            print('----LANE 2 EMERGENCY----')
            first = 1

        val[0] = int(lane)
        val[1] = int(sound)

        if val != temp:
            if val[0] == 1 and val[1] == 1:
                print('---EMERGENCY----')
                trigger = True

            for i in range(0, len(temp)):
                temp[i] = val[i]


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


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def subscribe(client: mqtt_client, s_topic):
    def on_message(client, userdata, msg):
        global lane, sound, lane_1, lane_2
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if msg.topic == 'em/lanes':
            lane = msg.payload.decode()
        elif msg.topic == 'em/sound':
            sound = msg.payload.decode()
        elif msg.topic == 'em/lane_1':
            lane_1 = msg.payload.decode()
        elif msg.topic == 'em/lane_2':
            lane_2 = msg.payload.decode()

    client.subscribe(s_topic)
    client.on_message = on_message


def handle_sigint(signalum, frame):
    sys.exit()


def task():
    print('Subsribe Thread Starting')
    try:
        client = connect_mqtt()
        subscribe(client, ambulance)
        subscribe(client, mqtt_lane_2)
        subscribe(client, mqtt_lane_1)
        subscribe(client, siren)
        client.loop_start()
    except KeyboardInterrupt:
        client.loop_stop()


if __name__ == '__main__':
    main()
