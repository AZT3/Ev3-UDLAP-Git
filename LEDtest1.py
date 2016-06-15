import ev3dev.ev3.Button as Button
import ev3dev.ev3.Leds as Leds

def main():

    while(True):
        if(Button.left==True):
            Leds.set(Leds.LEFT, GREEN)
        else:
            Leds.set(Leds.LEFT, RED)
        if(Button.right==True):
            Leds.set(Leds.RIGHT, GREEN)
        else:
            Leds.set(Leds.RIGHT, RED)

if __name__ == '__main__':
    main()
