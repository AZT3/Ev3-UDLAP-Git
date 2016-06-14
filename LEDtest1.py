from ev3dev import *

def main()
    while(True)
        if(Button.left())
            Leds.set(LEFT, GREEN)
        else
            LEds.set(LEFT, RED)
        if(Button.right())
            Leds.set(RIGHT, GREEN)
        else
            LEds.set(RIGHT, RED)

if __name__ == '__main__':
    main()
