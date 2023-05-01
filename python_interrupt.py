import random
import sys
from _thread import interrupt_main
from signal import SIGINT, signal
from threading import Thread
from time import sleep

from paho.mqtt import client as mqtt_client

broker = '192.168.1.8'
port = 1883
topic = "em/lanes"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def publish(client, text):
    while True:
        sleep(1)
        msg = f"message: {text}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

# handle single


def handle_sigint(signalnum, frame):

    # terminate
    print('Main interrupted! Exiting.')
    sys.exit()

# task executed in a new thread


def task():
    try:
        # block for a moment
        sleep(20)
        client = connect_mqtt()
        subscribe(client)
    # interrupt the main thread
        print('Interrupting main thread now')
        interrupt_main()
    except KeyboardInterrupt:
        sys.exit()


# register the signal handler for this process
signal(SIGINT, handle_sigint)
# start the new thread
thread = Thread(target=task)
thread.start()
# wait around

client = connect_mqtt
publish(client, 1)
while True:
    print('Main thread waiting...')
    sleep(0.5)
