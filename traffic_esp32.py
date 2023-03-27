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

#initiate 4 lanes
lane_1 = lane()
lane_2 = lane()
lane_3 = lane()
lane_4 = lane()

def main():
    
    green_1.value(0)
    yellow_1.value(0)
    red_1.value(0)

    while True: #cycle through 4 lanes
        
        lane_1_green()
        sleep(5)
        lane_1_yellow()
        sleep(3)
        
    
        lane_2_green()
        sleep(5)
        lane_2_yellow()
        sleep(3)
        lane_3_green()
        sleep(5)
        lane_3_yellow()
        sleep(3)
        '''
        lane_4_green()
        sleep(5)
        lane_4_yellow()
        sleep(3)
        '''
        
#function for displaying text
def display_lanes():
    
    print('Lane 1 Green:' + Fore.GREEN, lane_1.state, end=' ')
    print('\tLane 2 Green:', lane_2.state, end=' ')
    print('\tLane 3 Green:', lane_3.state, end=' ')
    print('\tLane 4 Green:', lane_4.state)
    print('Lane 1 Yellow:', lane_1.state, end=' ')
    print('\tLane 2 Yellow', lane_2.state, end=' ')
    print('\tLane 3 Yellow', lane_3.state, end=' ')
    print('\tLane 4 Yellow', lane_4.state)
    print('Lane 1 Red:', lane_1.state, end=' ')
    print('\tLane 2 Red:', lane_2.state, end=' ')
    print('\tLane 3 Red:', lane_3.state, end=' ')
    print('\tLane 4 Red:', lane_4.state)
    print('------------------------------------------')
    
def traffic_1_check():
    
    if lane_1.state == 3:
        print('Lane 1 state:', lane_1.state)
        green_1.value(1)
        yellow_1.value(0)
        red_1.value(0)
        
    elif lane_1.state == 2:
        print('Lane 1 state:', lane_1.state)
        green_1.value(0)
        yellow_1.value(1)
        red_1.value(0)
        
    elif lane_1.state == 1:
        print('Lane 1 state:', lane_1.state)
        
        green_1.value(0)
        yellow_1.value(0)
        red_1.value(1)

def traffic_2_check():
    if lane_2.state == 3:
        print('Lane 2 state:', lane_2.state)
        green_2.value(1)
        yellow_2.value(0)
        red_2.value(0)
        
    elif lane_2.state == 2:
        print('Lane 2 state:', lane_2.state)
        green_2.value(0)
        yellow_2.value(1)
        red_2.value(0)
        
    elif lane_2.state == 1:
        
        green_2.value(0)
        yellow_2.value(0)
        red_2.value(1)
   
def traffic_3_check():
    if lane_3.state == 3:
        green_3.value(1)
        yellow_3.value(0)
        red_3.value(0)
    elif lane_3.state == 2:
        green_3.value(0)
        yellow_3.value(0)
        red_3.value(1)
    elif lane_3.state == 1:
        green_3.value(0)
        yellow_3.value(0)
        red_3.value(1)
        
'''
    
def traffic_4_check():
    if lane_4.state == 3:
        green_1.value(0)
        yellow_1.value(0)
        red_1.value(1)
    elif lane_4.state == 2:
        green_1.value(0)
        yellow_1.value(0)
        red_1.value(1)
    elif lane_4.state == 1:
        green_1.value(0)
        yellow_1.value(0)
        red_1.value(1)
'''
#The following functions are for switching the lane status
def lane_1_green():
    lane_1.switch_green()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_red()
    
    traffic_1_check()
    traffic_2_check()
    #traffic_3_check()
    #traffic_4_check()
    
def lane_1_yellow():
    lane_1.switch_yellow()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_red()
    
    traffic_1_check()
    traffic_2_check()
    #traffic_3_check()
    #traffic_4_check()
    
def lane_2_green():
    lane_1.switch_red()
    lane_2.switch_green()
    lane_3.switch_red()
    lane_4.switch_red()
    
    traffic_1_check()
    traffic_2_check()
    #traffic_3_check()
    #traffic_4_check()
    
    
def lane_2_yellow():
    lane_1.switch_red()
    lane_2.switch_yellow()
    lane_3.switch_red()
    lane_4.switch_red()
    
    traffic_1_check()
    traffic_2_check()
    #traffic_3_check()
    #traffic_4_check()
    
def lane_3_green():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_green()
    lane_4.switch_red()
    
    traffic_1_check()
    traffic_2_check()
    #traffic_3_check()
    #traffic_4_check()
    
def lane_3_yellow():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_yellow()
    lane_4.switch_red()
    
    traffic_1_check()
    traffic_2_check()
    #traffic_3_check()
    #traffic_4_check()
    
def lane_4_green():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_green()
    
    traffic_1_check()
    traffic_2_check()
    #traffic_3_check()
    #traffic_4_check()
    
def lane_4_yellow():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_yellow()
    
    traffic_1_check()
    traffic_2_check()
    #traffic_3_check()
    #traffic_4_check()
    
if __name__ == "__main__":
    main()
