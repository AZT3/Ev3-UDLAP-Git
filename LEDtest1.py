import ev3dev

def main():
    while(True):
        if(ev3dev.ev3.Button.left==True):
            ev3dev.core.Leds.set(LEFT, GREEN)
        else:
            ev3dev.core.Leds.set(LEFT, RED)
        if(ev3.Button.right==True):
            ev3dev.core.Leds.set(RIGHT, GREEN)
        else:
            ev3dev.core.Leds.set(RIGHT, RED)

if __name__ == '__main__':
    main()
