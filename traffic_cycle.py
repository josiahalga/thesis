import colorama
import turtle
from colorama import Fore, Back, Style
from traffic import lane
from time import sleep

#initiate 4 lanes
lane_1 = lane()
lane_2 = lane()
lane_3 = lane()
lane_4 = lane()

pen_1 = turtle.Turtle()
red_light_1 = turtle.Turtle()
yellow_light_1 = turtle.Turtle()
green_light_1 = turtle.Turtle()

pen_2 = turtle.Turtle()
red_light_2 = turtle.Turtle()
yellow_light_2 = turtle.Turtle()
green_light_2 = turtle.Turtle()

pen_3 = turtle.Turtle()
red_light_3 = turtle.Turtle()
yellow_light_3 = turtle.Turtle()
green_light_3 = turtle.Turtle()

pen_4 = turtle.Turtle()
red_light_4 = turtle.Turtle()
yellow_light_4 = turtle.Turtle()
green_light_4 = turtle.Turtle()

def main():
    wn = turtle.Screen()
    wn.title('Traffic Light Simulation')
    wn.bgcolor('black')

    #draw
    pen_1.color('yellow')
    pen_1.width(3)
    pen_1.hideturtle()
    pen_1.penup()
    pen_1.goto(-30, 130)
    pen_1.pendown()
    pen_1.fd(60)
    pen_1.rt(90)
    pen_1.fd(120)
    pen_1.rt(90)
    pen_1.fd(60)
    pen_1.rt(90)
    pen_1.fd(120)

    #draw red
    red_light_1.shape('circle')
    red_light_1.color('grey')
    red_light_1.penup()
    red_light_1.goto(0, 110)

    #draw yellow
    yellow_light_1.shape('circle')
    yellow_light_1.color('grey')
    yellow_light_1.penup()
    yellow_light_1.goto(0, 70)
    
    #draw red
    green_light_1.shape('circle')
    green_light_1.color('grey')
    green_light_1.penup()
    green_light_1.goto(0, 30)
    
    #draw
    pen_2.color('yellow')
    pen_2.width(3)
    pen_2.hideturtle()
    pen_2.penup()
    pen_2.goto(40, 60)
    pen_2.pendown()
    pen_2.fd(60)
    pen_2.rt(90)
    pen_2.fd(120)
    pen_2.rt(90)
    pen_2.fd(60)
    pen_2.rt(90)
    pen_2.fd(120)

    #draw red
    red_light_2.shape('circle')
    red_light_2.color('grey')
    red_light_2.penup()
    red_light_2.goto(70, 40)

    #draw yellow
    yellow_light_2.shape('circle')
    yellow_light_2.color('grey')
    yellow_light_2.penup()
    yellow_light_2.goto(70, 0)
    
    #draw red
    green_light_2.shape('circle')
    green_light_2.color('grey')
    green_light_2.penup()
    green_light_2.goto(70, -40)
    
    #draw
    pen_3.color('yellow')
    pen_3.width(3)
    pen_3.hideturtle()
    pen_3.penup()
    pen_3.goto(-30, -10)
    pen_3.pendown()
    pen_3.fd(60)
    pen_3.rt(90)
    pen_3.fd(120)
    pen_3.rt(90)
    pen_3.fd(60)
    pen_3.rt(90)
    pen_3.fd(120)

    #draw red
    red_light_3.shape('circle')
    red_light_3.color('grey')
    red_light_3.penup()
    red_light_3.goto(0, -30)

    #draw yellow
    yellow_light_3.shape('circle')
    yellow_light_3.color('grey')
    yellow_light_3.penup()
    yellow_light_3.goto(0, -70)
    
    #draw red
    green_light_3.shape('circle')
    green_light_3.color('grey')
    green_light_3.penup()
    green_light_3.goto(0, -110)
    
    #draw
    pen_4.color('yellow')
    pen_4.width(3)
    pen_4.hideturtle()
    pen_4.penup()
    pen_4.goto(-100, 60)
    pen_4.pendown()
    pen_4.fd(60)
    pen_4.rt(90)
    pen_4.fd(120)
    pen_4.rt(90)
    pen_4.fd(60)
    pen_4.rt(90)
    pen_4.fd(120)

    #draw red
    red_light_4.shape('circle')
    red_light_4.color('grey')
    red_light_4.penup()
    red_light_4.goto(-70, 40)

    #draw yellow
    yellow_light_4.shape('circle')
    yellow_light_4.color('grey')
    yellow_light_4.penup()
    yellow_light_4.goto(-70, 0)
    
    #draw red
    green_light_4.shape('circle')
    green_light_4.color('grey')
    green_light_4.penup()
    green_light_4.goto(-70, -40)
    
    while True: #cycle through 4 lanes
        lane_1_green()
        display_lanes()
        green_light_1.color('green')
        sleep(5)
        lane_1_yellow()
        display_lanes()
        yellow_light_1.color('yellow')
        green_light_1.color('grey')
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
        
    wn.mainloop()
        
#function for displaying text
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
    
def traffic_1_green():
    red_light_1.color('grey')
    yellow_light_1.color('grey')
    green_light_1.color('green')

def traffic_1_yellow():
    red_light_1.color('grey')
    yellow_light_1.color('yellow')
    green_light_1.color('grey')
    
def traffic_1_red():
    red_light_1.color('red')
    yellow_light_1.color('grey')
    green_light_1.color('grey')
    
def traffic_2_green():
    red_light_2.color('grey')
    yellow_light_2.color('grey')
    green_light_2.color('green')

def traffic_2_yellow():
    red_light_2.color('grey')
    yellow_light_2.color('yellow')
    green_light_2.color('grey')

def traffic_2_red():
    red_light_2.color('red')
    yellow_light_2.color('grey')
    green_light_2.color('grey')
    
def traffic_3_green():
    red_light_3.color('grey')
    yellow_light_3.color('grey')
    green_light_3.color('green')

def traffic_3_yellow():
    red_light_3.color('grey')
    yellow_light_3.color('yellow')
    green_light_3.color('grey')

def traffic_3_red():
    red_light_3.color('red')
    yellow_light_3.color('grey')
    green_light_3.color('grey')
    
def traffic_4_green():
    red_light_4.color('grey')
    yellow_light_4.color('grey')
    green_light_4.color('green')

def traffic_4_yellow():
    red_light_4.color('grey')
    yellow_light_4.color('yellow')
    green_light_4.color('grey')

def traffic_4_red():
    red_light_4.color('red')
    yellow_light_4.color('grey')
    green_light_4.color('grey')

#The following functions are for switching the lane status
def lane_1_green():
    lane_1.switch_green()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_red()
    traffic_1_green()
    traffic_2_red()
    traffic_3_red()
    traffic_4_red()
    
def lane_1_yellow():
    lane_1.switch_yellow()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_red()
    traffic_1_yellow()
    traffic_2_red()
    traffic_3_red()
    traffic_4_red()
    
def lane_2_green():
    lane_1.switch_red()
    lane_2.switch_green()
    lane_3.switch_red()
    lane_4.switch_red()
    traffic_1_red()
    traffic_2_green()
    traffic_3_red()
    traffic_4_red()
    
    
def lane_2_yellow():
    lane_1.switch_red()
    lane_2.switch_yellow()
    lane_3.switch_red()
    lane_4.switch_red()
    traffic_1_red()
    traffic_2_yellow()
    traffic_3_red()
    traffic_4_red()
    
def lane_3_green():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_green()
    lane_4.switch_red()
    traffic_1_red()
    traffic_2_red()
    traffic_3_green()
    traffic_4_red()
    
def lane_3_yellow():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_yellow()
    lane_4.switch_red()
    traffic_1_red()
    traffic_2_red()
    traffic_3_yellow()
    traffic_4_red()
    
def lane_4_green():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_green()
    
    traffic_1_red()
    traffic_2_red()
    traffic_3_red()
    traffic_4_green()
    
def lane_4_yellow():
    lane_1.switch_red()
    lane_2.switch_red()
    lane_3.switch_red()
    lane_4.switch_yellow()
    
    traffic_1_red()
    traffic_2_red()
    traffic_3_red()
    traffic_4_yellow()
    
if __name__ == "__main__":
    main()