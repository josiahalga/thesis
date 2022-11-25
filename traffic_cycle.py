import colorama
from colorama import Fore, Back, Style
from traffic import lane
from time import sleep

lane_1 = lane()
lane_2 = lane()
lane_3 = lane()
lane_4 = lane()

def main():
    
    while True:
        lane_1_green()
        display_lanes()
        sleep(30)
        lane_1_yellow()
        display_lanes()
        sleep(3)
        lane_2_green()
        display_lanes()
        sleep(30)
        lane_2_yellow()
        display_lanes()
        sleep(3)
        lane_3_green()
        display_lanes()
        sleep(30)
        lane_3_yellow()
        display_lanes()
        sleep(3)
        lane_4_green()
        display_lanes()
        sleep(30)
        lane_4_yellow()
        display_lanes()
        sleep(3)
        
def display_lanes():
        
    colorama.init(autoreset=True)
    
    print(Fore.GREEN + 'Lane 1 Green:' + Fore.GREEN, lane_1.green, end=' ')
    print(Fore.GREEN + '\tLane 2 Green:', lane_2.green, end=' ')
    print(Fore.GREEN + '\tLane 3 Green:', lane_3.green, end=' ')
    print(Fore.GREEN + '\tLane 4 Green:', lane_4.green)
    print(Fore.YELLOW + 'Lane 1 Yellow:', lane_1.yellow, end=' ')
    print(Fore.YELLOW + '\tLane 2 Yellow', lane_2.yellow, end=' ')
    print(Fore.YELLOW + '\tLane 3 Yellow', lane_3.yellow, end=' ')
    print(Fore.YELLOW + '\tLane 4 Yellow', lane_4.yellow)
    print(Fore.RED + 'Lane 1 Red:', lane_1.red, end=' ')
    print(Fore.RED + '\tLane 2 Red:', lane_2.red, end=' ')
    print(Fore.RED + '\tLane 3 Red:', lane_3.red, end=' ')
    print(Fore.RED + '\tLane 4 Red:', lane_4.red)
    print('------------------------------------------')

def lane_1_green():
    lane_1.switch_green()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_red()
    
def lane_1_yellow():
    lane_1.switch_yellow()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_red()
    
def lane_2_green():
    lane_1.switch_red()
    lane_2.switch_green()
    lane_3.switch_red()
    lane_4.switch_red()
    
def lane_2_yellow():
    lane_1.switch_red()
    lane_2.switch_yellow()
    lane_3.switch_red()
    lane_4.switch_red()
    
def lane_3_green():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_green()
    lane_4.switch_red()
    
def lane_3_yellow():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_yellow()
    lane_4.switch_red()
    
def lane_4_green():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_green()
    
def lane_4_yellow():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_yellow()
    
if __name__ == "__main__":
    main()