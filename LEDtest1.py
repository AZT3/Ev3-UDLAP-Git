from ev3dev import *

def main():
    while(True):
        if(ev3.Button.left==True):
            core.Leds.set(LEFT, GREEN)
        else:
            core.Leds.set(LEFT, RED)
        if(ev3.Button.right==True):
            core.Leds.set(RIGHT, GREEN)
        else:
            core.Leds.set(RIGHT, RED)

if __name__ == '__main__':
    main()
