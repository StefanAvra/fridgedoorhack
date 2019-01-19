import utime
from machine import Pin
import os
import uasyncio
import set_time

BUTTON_PIN = 14
BUZZER_PIN = 12
BLINK = False
ENABLE_LOG = False
LEGIT_OPEN_TIME = 10  # how many seconds it is ok to keep the fridge open

opened_counter = 0
door_open = False
loop = uasyncio.get_event_loop()

led = Pin(2, Pin.OUT)  # on-board LED
pin = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)


if ENABLE_LOG:
    if 'logs' not in os.listdir():
        os.mkdir('logs')
    log = open('logs/door.log', 'a')  # todo: has to be closed and re-opened. make async


async def play_melody():
    pass


async def door_opened():
    # play opening sound
    print('door opened')
    global opened_counter
    opened_counter += 1
    led.off()
    await uasyncio.sleep(LEGIT_OPEN_TIME)
    print('close the door!!111')
    # start 'forgot to close'-code if still open


async def door_closed():
    # todo: cancel door_opened
    # play closing sound
    print('door closed')
    led.on()
    # do logging


async def check_door():
    global door_open
    global opened_counter
    global loop
    while True:
        print('checking door', str(opened_counter))
        await uasyncio.sleep_ms(100)
        if not pin.value() == door_open:
            await uasyncio.sleep_ms(100)  # debouncing
            if not pin.value() == door_open:
                door_open = pin.value()
                if door_open:
                    loop.create_task(door_opened())
                    # await door_opened()
                else:
                    loop.create_task(door_closed())
                    # await door_closed()


def main():
    global loop
    loop.create_task(set_time.keep_time_synced())
    loop.create_task(check_door())
    loop.run_forever()


if __name__ == '__main__':
    main()
