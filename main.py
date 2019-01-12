import time
from machine import Pin
import os

BUTTON_PIN = 14
BUZZER_PIN = 12
BLINK = False
ENABLE_LOG = False

led = Pin(2, Pin.OUT)  # on-board LED
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

if ENABLE_LOG:
    if 'logs' not in os.listdir():
        os.mkdir('logs')
    log = open('logs/door.log', 'a')  # has to be closed somewhere (and re-opened, so it should be moved to main())


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
