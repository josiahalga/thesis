import ubinascii
import machine
import micropython
import network
import esp
import gc
import _thread
gc.collect()

from time import sleep
from machine import Pin
from traffic import lane
from umqttsimple import MQTTClient

ssid = 'Alga_2.4GHz'
password = 'Algafamily123!'
client = None
mqtt_server = '192.168.1.10'

mqtt_lane_1 = 0
mqtt_lane_2 = 0
mqtt_lane_3 = 0
mqtt_lane_4 = 0
mqtt_sound = 0

emergency_status = False
emergency_lane = 0

semaphore = _thread.allocate_lock()

client_id = ubinascii.hexlify(machine.unique_id())

detection_lane_1 = "em/lane_1"
detection_lane_2 = "em/lane_2"
detection_lane_3 = "em/lane_3"
detection_lane_4 = "em/lane_4"
siren = "em/sound"

last_message = 0
message_interval = 5

def my_thread_func():
    global client
    
    station = network.WLAN(network.STA_IF)

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass
    
    try:
        client = connect_mqtt()
    except OSError as e:
        restart_and_reconnect()
        
    while True:
        try:
            msg = client.check_msg()
            sleep(0.01)
        except OSError as e:
            restart_and_reconnect()

def connect_mqtt():
  global client_id, mqtt_server
  print('---Connecting to Broker---')
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(subscribe_callback)
  client.connect()
  client.subscribe(detection_lane_1)
  client.subscribe(detection_lane_2)
  client.subscribe(detection_lane_3)
  client.subscribe(detection_lane_4)
  client.subscribe(siren)
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(5)
  machine.reset()
  
def subscribe_callback(topic, msg):
    global mqtt_lane_1, mqtt_lane_2, mqtt_lane_3, mqtt_lane_4, mqtt_sound
    msg = msg.decode('UTF-8')
    #print(msg, topic)
    topic = topic.decode('UTF-8')
    if topic == 'em/lane_1':
        #print('lane:1 ', msg)
        mqtt_lane_1 = int(msg)
    elif topic == 'em/lane_2':
        mqtt_lane_2 = int(msg)
    elif topic == 'em/lane_3':
        mqtt_lane_3 = int(msg)
    elif topic == 'em/lane_4':
        mqtt_lane_4 = int(msg)
    elif topic == 'em/sound':
        mqtt_sound = int(msg)

def my_interrupt_handler(timer):
    global mqtt_lane_1, mqtt_lane_2, mqtt_lane_3, mqtt_lane_4, mqtt_sound, emergency_status, emergency_lane, emergency_status_pin
    global client

    if mqtt_sound == 0:
        if emergency_status:
            emergency_status = False

    if mqtt_lane_1 == 0:
        if emergency_status:
            emergency_status = False
            mqtt_lane_1 = 0
            lane_1_yellow()
    elif mqtt_lane_2 == 0:
        if emergency_status:
            emergency_status = False
            mqtt_lane_2 = 0
            lane_2_yellow()
    elif mqtt_lane_3 == 0:
        if emergency_status:
            emergency_status = False
            mqtt_lane_3 = 0
            lane_3_yellow()
    elif mqtt_lane_4 == 0:
        if emergency_status:
            emergency_status = False
            mqtt_lane_4 = 0
            lane_4_yellow()

        # SIREN FIRST DETECTION
    if mqtt_sound == 1:
            # print('AMBULANCE SIREN DETECTED')
        if mqtt_lane_1 == 1:
            if not emergency_status:
                emergency_status = True
                emergency_lane = 0
        elif mqtt_lane_2 == 1:
            if not emergency_status:
                emergency_status = True
                emergency_lane = 1
        elif mqtt_lane_3 == 1:
            if not emergency_status:
                emergency_status = True
                emergency_lane = 2
        elif mqtt_lane_4 == 1:
            if not emergency_status:
                emergency_status = True
                emergency_lane = 3

        # AMBULANCE FIRST DETECTION
    if mqtt_lane_1 == 1:
        if mqtt_sound == 1:
            if not emergency_status:
                emergency_status = True
                emergency_lane = 0
    elif mqtt_lane_2 == 1:
        if mqtt_sound == 1:
            if not emergency_status:
                emergency_status = True
                emergency_lane = 1
    elif mqtt_lane_3 == 1:
        if mqtt_sound == 1:
            if not emergency_status:
                emergency_status = True
                emergency_lane = 2
    elif mqtt_lane_4 == 1:
        if mqtt_sound == 1:
            if not emergency_status:
                emergency_status = True
                emergency_lane = 3

    if emergency_status:
        client.publish('em/emergency', '1')
        emergency_status_pin.value(1)
        if emergency_lane == 0:
            lane_1_green()
            print('EMERGENCY ON LANE 1')
            client.publish('em/lanes', '1')
            sleep(0.1)
        elif emergency_lane == 1:
            lane_2_green()
            print('EMERGENCY ON LANE 2')
            client.publish('em/lanes', '2')
            sleep(0.1)
        elif emergency_lane == 2:
            lane_3_green()
            print('EMERGENCY ON LANE 3')
            client.publish('em/lanes', '3')
            sleep(0.1)
        elif emergency_lane == 3:
            lane_4_green()
            print('EMERGENCY ON LANE 4')
            client.publish('em/lanes', '4')
            sleep(0.1)
    else:
        sleep(0.1)
        client.publish('em/emergency', '0')
        client.publish('em/lanes', '0')
        emergency_status_pin.value(0)

# Emergency Interrupt
em_1 = False
em_2 = False
em_3 = False
em_4 = False

def ep_1_interrupt():
    global mqtt_lane_1

    while True:
        if mqtt_lane_1 == 0:
            lane_1_yellow()
            break
        else:
            lane_1_green()
            print('EMERGENCY ON LANE 1')
            sleep(5)

def ep_2_interrupt():
    global mqtt_lane_2

    while True:
        if mqtt_lane_2 == 0:
            lane_2_yellow()
            break
        else:
            lane_2_green()
            print('EMERGENCY ON LANE 2')
            sleep(5)


def ep_3_interrupt():
    global mqtt_lane_3

    while True:
        if mqtt_lane_3 == 0:
            lane_3_yellow()
            break
        else:
            lane_3_green()
            print('EMERGENCY ON LANE 3')
            sleep(5)


def ep_4_interrupt():
    global mqtt_lane_4

    while True:
        if mqtt_lane_4 == 0:
            lane_4_yellow()
            break
        else:
            lane_4_green()
            print('EMERGENCY ON LANE 4')
            sleep(5)


# Emergency Pins
ep_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)
ep_2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
ep_3 = Pin(19, Pin.IN, Pin.PULL_DOWN)
ep_4 = Pin(2, Pin.IN, Pin.PULL_DOWN)

emergency_status_pin = Pin(18, Pin.OUT)


# Interrupt Handler
#ep_1.irq(trigger=Pin.IRQ_RISING, handler=ep_1_interrupt)
ep_2.irq(trigger=Pin.IRQ_RISING, handler=ep_2_interrupt)
ep_3.irq(trigger=Pin.IRQ_RISING, handler=ep_3_interrupt)
ep_4.irq(trigger=Pin.IRQ_RISING, handler=ep_4_interrupt)

# Lane 1
lane_1_green = 21
lane_1_yellow = 22
lane_1_red = 23

red_1 = Pin(lane_1_red, Pin.OUT)
yellow_1 = Pin(lane_1_yellow, Pin.OUT)
green_1 = Pin(lane_1_green, Pin.OUT)

# Lane 2
lane_2_green = 15
lane_2_yellow = 16
lane_2_red = 17

red_2 = Pin(lane_2_red, Pin.OUT)
yellow_2 = Pin(lane_2_yellow, Pin.OUT)
green_2 = Pin(lane_2_green, Pin.OUT)

# Lane 3
lane_3_green = 14
lane_3_yellow = 12
lane_3_red = 13

red_3 = Pin(lane_3_red, Pin.OUT)
yellow_3 = Pin(lane_3_yellow, Pin.OUT)
green_3 = Pin(lane_3_green, Pin.OUT)

# Lane 4
lane_4_green = 32
lane_4_yellow = 33
lane_4_red = 25

red_4 = Pin(lane_4_red, Pin.OUT)
yellow_4 = Pin(lane_4_yellow, Pin.OUT)
green_4 = Pin(lane_4_green, Pin.OUT)

# initiate 4 lanes
lane_1 = lane()
lane_2 = lane()
lane_3 = lane()
lane_4 = lane()


def main():

    global em_1
    global em_2
    global em_3
    global em_4
    global client

    green_1.value(0)
    yellow_1.value(0)
    red_1.value(0)
    
    _thread.start_new_thread(my_thread_func, ())

    print('Connection successful')
    
    sleep(4)
    
    timer = machine.Timer(0)

    timer.init(period=100, mode=machine.Timer.PERIODIC, callback=my_interrupt_handler)
    
    print('Thread Started')
    
    print('Starting Traffic Light Sequence')
    
    print('-----------------')

    while True:  # cycle through 4 lanes

        lane_1_green()
        sleep(10)
        lane_1_yellow()
        sleep(3)
        lane_2_green()
        sleep(10)
        lane_2_yellow()
        sleep(3)
        lane_3_green()
        sleep(10)
        lane_3_yellow()
        sleep(3)
        lane_4_green()
        sleep(10)
        lane_4_yellow()
        sleep(3)
        
        print('---Cycle Complete---\n')

def traffic_1_check():

    if lane_1.state == 3:
        print('Lane 1: Green')
        green_1.value(1)
        yellow_1.value(0)
        red_1.value(0)

    elif lane_1.state == 2:
        green_1.value(0)
        yellow_1.value(1)
        red_1.value(0)

    elif lane_1.state == 1:

        green_1.value(0)
        yellow_1.value(0)
        red_1.value(1)


def traffic_2_check():
    if lane_2.state == 3:
        print('Lane 2: Green')
        green_2.value(1)
        yellow_2.value(0)
        red_2.value(0)

    elif lane_2.state == 2:
        green_2.value(0)
        yellow_2.value(1)
        red_2.value(0)

    elif lane_2.state == 1:

        green_2.value(0)
        yellow_2.value(0)
        red_2.value(1)


def traffic_3_check():
    if lane_3.state == 3:
        print('Lane 3 Green')

        green_3.value(1)
        yellow_3.value(0)
        red_3.value(0)
    elif lane_3.state == 2:

        green_3.value(0)
        yellow_3.value(1)
        red_3.value(0)
    elif lane_3.state == 1:

        green_3.value(0)
        yellow_3.value(0)
        red_3.value(1)


def traffic_4_check():
    if lane_4.state == 3:
        print('Lane 4: Green')
        green_4.value(1)
        yellow_4.value(0)
        red_4.value(0)
    elif lane_4.state == 2:
        green_4.value(0)
        yellow_4.value(1)
        red_4.value(0)
    elif lane_4.state == 1:
        green_4.value(0)
        yellow_4.value(0)
        red_4.value(1)

# The following functions are for switching the lane status


def lane_1_green():
    lane_1.switch_green()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_red()

    traffic_1_check()
    traffic_2_check()
    traffic_3_check()
    traffic_4_check()


def lane_1_yellow():
    lane_1.switch_yellow()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_red()

    traffic_1_check()
    traffic_2_check()
    traffic_3_check()
    traffic_4_check()


def lane_2_green():
    lane_1.switch_red()
    lane_2.switch_green()
    lane_3.switch_red()
    lane_4.switch_red()

    traffic_1_check()
    traffic_2_check()
    traffic_3_check()
    traffic_4_check()


def lane_2_yellow():
    lane_1.switch_red()
    lane_2.switch_yellow()
    lane_3.switch_red()
    lane_4.switch_red()

    traffic_1_check()
    traffic_2_check()
    traffic_3_check()
    traffic_4_check()


def lane_3_green():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_green()
    lane_4.switch_red()

    traffic_1_check()
    traffic_2_check()
    traffic_3_check()
    traffic_4_check()


def lane_3_yellow():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_yellow()
    lane_4.switch_red()

    traffic_1_check()
    traffic_2_check()
    traffic_3_check()
    traffic_4_check()


def lane_4_green():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_green()

    traffic_1_check()
    traffic_2_check()
    traffic_3_check()
    traffic_4_check()


def lane_4_yellow():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_yellow()

    traffic_1_check()
    traffic_2_check()
    traffic_3_check()
    traffic_4_check()


if __name__ == "__main__":
    main()


