import ev3dev.ev3 as ev3

def main():
    LEFT=ev3.Leds.LEFT
    RIGHT=ev3.Leds.RIGHT
    GREEN=ev3.Leds.GREEN
    RED=ev3.Leds.RED
    Screen=ev3.core.Screen
    ev3.Leds.all_off()
    while(True):
        Screen.clear()
        Screen.draw.text([5,20,200,100],String(ev3.Button.LEFT))
        Screen.draw.text([5,50,200,100],String(ev3.Button.RIGHT))

        if(ev3.Button.left==True):
            ev3.Leds.set_color(LEFT, GREEN)
        else:
            ev3.Leds.set_color(LEFT, RED)
        if(ev3.Button.right==True):
            ev3.Leds.set_color(RIGHT, GREEN)
        else:
            ev3.Leds.set_color(RIGHT, RED)

if __name__ == '__main__':
    main()
