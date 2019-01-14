import utime
from machine import Pin
import os
import uasyncio
import set_time
from aswitch import Switch

BUTTON_PIN = 14
BUZZER_PIN = 12
BLINK = False
ENABLE_LOG = False
LEGIT_OPEN_TIME = 90  # how many seconds it is ok to keep the fridge open

door_open = False

led = Pin(2, Pin.OUT)  # on-board LED
pin = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

switch = Switch(pin)

if ENABLE_LOG:
    if 'logs' not in os.listdir():
        os.mkdir('logs')
    log = open('logs/door.log', 'a')  # todo: has to be closed and re-opened. make async


def is_door_open():
    global door_open
    if not pin.value():
        door_open = False
    else:
        utime.sleep_ms(300)  # debouncing
        if pin.value():
            door_open = True

    return door_open


def play_melody():
    pass


def main():
    done = False
    while not done:
        if is_door_open():
            led.off()  # weird, on/off is swapped
            if BLINK:
                utime.sleep_ms(50)
                led.on()

            if ENABLE_LOG:
                log.write("door opened")

            utime.sleep(2)
        else:
            led.on()
            if ENABLE_LOG:
                log.write('door closed')
            utime.sleep_ms(100)
            while not pin.value():
                pass


async def door_opened():
    # play opening sound
    led.off()
    await uasyncio.sleep(LEGIT_OPEN_TIME)
    # start 'forgot to close'-code if still open


async def door_closed():
    # play closing sound
    led.on()
    # do logging
    pass


def main2():
    switch.close_func(door_closed())
    switch.open_func(door_opened())
    loop = uasyncio.get_event_loop()
    loop.create_task(set_time.keep_time_synced())
    loop.run_forever()


if __name__ == '__main__':
    main2()
