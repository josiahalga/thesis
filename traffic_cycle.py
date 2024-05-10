# RUN ON ESP32 USING THONNY
from traffic import lane
from machine import Pin
from time import sleep
# Lane 1
lane_1_green = 21
lane_1_yellow = 22
lane_1_red = 23

red_1 = Pin(lane_1_red, Pin.OUT)
yellow_1 = Pin(lane_1_yellow, Pin.OUT)
green_1 = Pin(lane_1_green, Pin.OUT)

#initiate 4 lanes
lane_1 = lane()
lane_2 = lane()
lane_3 = lane()
lane_4 = lane()

def main():

    while True: #cycle through 4 lanes
        lane_1_green()
        display_lanes()
        sleep(5)
        lane_1_yellow()
        display_lanes()
        sleep(3)
        lane_2_green()
        display_lanes()
        sleep(5)
        lane_2_yellow()
        display_lanes()
        sleep(3)
        lane_3_green()
        display_lanes()
        sleep(5)
        lane_3_yellow()
        display_lanes()
        sleep(3)
        lane_4_green()
        display_lanes()
        sleep(5)
        lane_4_yellow()
        display_lanes()
        sleep(3)
        
#function for displaying text
def display_lanes():
        
    colorama.init(autoreset=True)
    
    print(Fore.GREEN + 'Lane 1 Green:' + Fore.GREEN, lane_1.state, end=' ')
    print(Fore.GREEN + '\tLane 2 Green:', lane_2.state, end=' ')
    print(Fore.GREEN + '\tLane 3 Green:', lane_3.state, end=' ')
    print(Fore.GREEN + '\tLane 4 Green:', lane_4.state)
    print(Fore.YELLOW + 'Lane 1 Yellow:', lane_1.state, end=' ')
    print(Fore.YELLOW + '\tLane 2 Yellow', lane_2.state, end=' ')
    print(Fore.YELLOW + '\tLane 3 Yellow', lane_3.state, end=' ')
    print(Fore.YELLOW + '\tLane 4 Yellow', lane_4.state)
    print(Fore.RED + 'Lane 1 Red:', lane_1.state, end=' ')
    print(Fore.RED + '\tLane 2 Red:', lane_2.state, end=' ')
    print(Fore.RED + '\tLane 3 Red:', lane_3.state, end=' ')
    print(Fore.RED + '\tLane 4 Red:', lane_4.state)
    print('------------------------------------------')
    
def traffic_1_check():
    
    if lane_1.state == 3:
        green_1.value(1)
        yellow_1.value(0)
        red_1.value(0)
        
        red_light_1.color('grey')
        yellow_light_1.color('grey')
        green_light_1.color('green')
    elif lane_1.state == 2:
        green_1.value(0)
        yellow_1.value(1)
        red_1.value(0)
        
        red_light_1.color('grey')
        yellow_light_1.color('yellow')
        green_light_1.color('grey')
    elif lane_1.state == 1:
        green_1.value(0)
        yellow_1.value(0)
        red_1.value(1)
        
        red_light_1.color('red')
        yellow_light_1.color('grey')
        green_light_1.color('grey')
    
def traffic_2_check():
    if lane_2.state == 3:
        red_light_2.color('grey')
        yellow_light_2.color('grey')
        green_light_2.color('green')
    elif lane_2.state == 2:
        red_light_2.color('grey')
        yellow_light_2.color('yellow')
        green_light_2.color('grey')
    elif lane_2.state == 1:
        red_light_2.color('red')
        yellow_light_2.color('grey')
        green_light_2.color('grey')

    
def traffic_3_check():
    if lane_3.state == 3:
        red_light_3.color('grey')
        yellow_light_3.color('grey')
        green_light_3.color('green')
    elif lane_3.state == 2:
        red_light_3.color('grey')
        yellow_light_3.color('yellow')
        green_light_3.color('grey')
    elif lane_3.state == 1:
        red_light_3.color('red')
        yellow_light_3.color('grey')
        green_light_3.color('grey')
    
def traffic_4_check():
    if lane_4.state == 3:
        red_light_4.color('grey')
        yellow_light_4.color('grey')
        green_light_4.color('green')
    elif lane_4.state == 2:
        red_light_4.color('grey')
        yellow_light_4.color('yellow')
        green_light_4.color('grey')
    elif lane_4.state == 1:
        red_light_4.color('red')
        yellow_light_4.color('grey')
        green_light_4.color('grey')

#The following functions are for switching the lane status
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