import ev3dev.ev3 as ev3
import ev3dev.core as core

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
