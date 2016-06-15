import ev3dev.ev3 as ev3

def main():
    LEFT=ev3.Leds.LEFT
    RIGHT=ev3.Leds.RIGHT
    GREEN=ev3.Leds.GREEN
    RED=ev3.Leds.RED
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
