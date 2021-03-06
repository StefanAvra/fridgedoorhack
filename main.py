import utime
from machine import Pin
import os
import uasyncio
import set_time
import door_state
import buzzer_music
import config


opened_counter = 0
door_state.is_open = 0
door_open = False
loop = uasyncio.get_event_loop()

led = Pin(2, Pin.OUT)  # on-board LED
pin = Pin(config.BUTTON_PIN, Pin.IN, Pin.PULL_UP)


if config.ENABLE_LOG:
    if 'logs' not in os.listdir():
        os.mkdir('logs')
        log = open('logs/door.log', 'w')
        log.write('action;time')
        log.close()

    async def log_door(action, time):
        log = open('logs/door.log', 'a')
        log.write(action + ';' + str("{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(*time)) + '\n')
        log.close()


async def play_melody(song_name):
    if song_name == 'random':
        song_name = buzzer_music.get_random_song()
    print('Playing "{}"...'.format(song_name))
    loop.create_task(log_door('playing: {}'.format(song_name), utime.localtime()))
    await buzzer_music.play_song(song_name)


async def play_sfx(song_name):
    if song_name == 'random':
        song_name = buzzer_music.get_random_song()
    print('Playing "{}"...'.format(song_name))
    loop.create_task(log_door('playing: {}'.format(song_name), utime.localtime()))
    await buzzer_music.play_completely(song_name)


async def door_opened():
    global opened_counter
    door_state.is_open += 1
    opened_counter += 1
    do_reset = False
    if opened_counter == config.COUNTER_MAX and config.ONE_UP:
        await play_sfx('1up')
        do_reset = True
    token = opened_counter
    print('door opened')
    if config.ENABLE_LOG:
        loop.create_task(log_door('opened', utime.localtime()))
    led.off()
    await uasyncio.sleep(config.LEGIT_OPEN_TIME)
    # start 'forgot to close'-code if still open
    # if door_state.is_open > 0 and token == opened_counter:
    while door_state.is_open > 0 and token == opened_counter:
        print('Close the door!!111')
        await play_melody('random')
        await uasyncio.sleep(3)
    print('Door has been opened {} times since last reset.\n'.format(opened_counter))
    if do_reset:
        do_reset = False
        opened_counter = 0


async def door_closed():
    door_state.is_open -= 1
    print('door closed')
    await uasyncio.sleep_ms(100)
    if config.CLOSING_SOUND:
        await play_sfx('closed')
    if config.ENABLE_LOG:
        loop.create_task(log_door('closed', utime.localtime()))
    led.on()


async def check_door():
    global door_open
    global opened_counter
    global loop
    while True:
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
