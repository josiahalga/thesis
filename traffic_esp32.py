from time import sleep

from machine import Pin

from traffic import lane

# Emergency Interrupt
em_1 = False
em_2 = False
em_3 = False
em_4 = False

def ep_1_interrupt(pin):

    while True:
        if pin.value() == 0:
            lane_1_yellow()
            break
        else:
            lane_1_green()
            print('EMERGENCY ON LANE 1')
            sleep(0.1)

def ep_2_interrupt(pin):

    while True:
        if pin.value() == 0:
            lane_2_yellow()
            break
        else:
            lane_2_green()
            print('EMERGENCY ON LANE 2')
            sleep(0.1)


def ep_3_interrupt(pin):

    while True:
        if pin.value() == 0:
            lane_3_yellow()
            break
        else:
            lane_3_green()
            print('EMERGENCY ON LANE 3')
            sleep(0.1)


def ep_4_interrupt(pin):

    while True:
        if pin.value() == 0:
            lane_4_yellow()
            break
        else:
            lane_4_green()
            print('EMERGENCY ON LANE 4')
            sleep(0.1)


# Emergency Pins
ep_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)
ep_2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
ep_3 = Pin(19, Pin.IN, Pin.PULL_DOWN)
ep_4 = Pin(2, Pin.IN, Pin.PULL_DOWN)


# Interrupt Handler
ep_1.irq(trigger=Pin.IRQ_RISING, handler=ep_1_interrupt)
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

    green_1.value(0)
    yellow_1.value(0)
    red_1.value(0)

    while True:  # cycle through 4 lanes

        lane_1_green()
        print(em_1)
        sleep(5)
        lane_1_yellow()
        sleep(3)
        lane_2_green()
        print(em_1)
        sleep(5)
        lane_2_yellow()
        sleep(3)
        lane_3_green()
        print(em_1)
        sleep(5)
        lane_3_yellow()
        sleep(3)
        lane_4_green()
        print(em_1)
        sleep(5)
        lane_4_yellow()
        sleep(3)

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
