import time
from machine import Pin

BUTTON_PIN = 14
BLINK = False
ENABLE_LOG = False

led = Pin(2, Pin.OUT)  # on-board LED
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

if ENABLE_LOG:
    log = open("door.log", "w")


def is_door_open():
    global door_open
    if not button.value():
        door_open = False
    else:
        time.sleep_ms(300)  # debouncing
        if button.value():
            door_open = True

    return door_open


def main():
    done = False
    while not done:
        if is_door_open():
            led.off()  # weird, on/off is swapped
            if BLINK:
                time.sleep_ms(50)
                led.on()

            if ENABLE_LOG:
                log.write("door opened")

            time.sleep(2)
        else:
            led.on()
            if ENABLE_LOG:
                log.write('door closed')
            time.sleep_ms(100)
            while not button.value():
                pass


if __name__ == '__main__':
    main()
