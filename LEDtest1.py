import ev3dev.ev3 as ev3
import ev3dev.core as core

def main():
    while(True):
        if(ev3.Button.left==True):
            ev3.Leds.set(LEFT, GREEN)
        else:
            ev3.Leds.set(LEFT, RED)
        if(ev3.Button.right==True):
            ev3.Leds.set(RIGHT, GREEN)
        else:
            ev3.Leds.set(RIGHT, RED)

if __name__ == '__main__':
    main()
