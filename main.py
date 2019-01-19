import utime
from machine import Pin
import os
import uasyncio
import set_time

BUTTON_PIN = 14
BUZZER_PIN = 12
BLINK = False
ENABLE_LOG = True
LEGIT_OPEN_TIME = 10  # how many seconds it is ok to keep the fridge open

opened_counter = 0
is_open = 0
door_open = False
loop = uasyncio.get_event_loop()

led = Pin(2, Pin.OUT)  # on-board LED
pin = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)


if ENABLE_LOG:
    if 'logs' not in os.listdir():
        os.mkdir('logs')
        log = open('logs/door.log', 'w')
        log.write('action;time')
        log.close()

    async def log_door(action, time):
        log = open('logs/door.log', 'a')
        log.write(action + ';' + str("{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(*time)) + '\n')
        log.close()


async def play_melody():
    pass


async def door_opened():
    global opened_counter
    global is_open
    is_open += 1
    opened_counter += 1
    token = opened_counter
    # play opening sound
    print('door opened')
    if ENABLE_LOG:
        loop.create_task(log_door('opened', utime.localtime()))
    led.off()
    await uasyncio.sleep(LEGIT_OPEN_TIME)
    # start 'forgot to close'-code if still open
    if is_open > 0 and token == opened_counter:
        print('close the door!!111')


async def door_closed():
    global is_open
    is_open -= 1
    print('door closed')
    # play closing sound
    if ENABLE_LOG:
        loop.create_task(log_door('closed', utime.localtime()))
    led.on()
    # do logging


async def check_door():
    global door_open
    global opened_counter
    global loop
    while True:
        print('Checking door...\nDoor has been opened %d times since last reset.' % opened_counter)
        await uasyncio.sleep_ms(100)
        if not pin.value() == door_open:
            await uasyncio.sleep_ms(100)  # debouncing
            if not pin.value() == door_open:
                door_open = pin.value()
                if door_open:
                    loop.create_task(door_opened())
                else:
                    loop.create_task(door_closed())


def main():
    global loop
    loop.create_task(set_time.keep_time_synced())
    loop.create_task(check_door())
    loop.run_forever()


if __name__ == '__main__':
    main()
