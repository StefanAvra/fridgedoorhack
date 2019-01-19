from rtttl import RTTTL
import songs
import utime
import uasyncio
import door_state
import config

from machine import Pin, PWM

buz_tim = PWM(Pin(config.BUZZER_PIN))


async def play_tone(freq, msec):
    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    if freq > 0:
        buz_tim.freq(int(freq))
        buz_tim.duty(50)
    await uasyncio.sleep_ms(int(msec * 0.9))
    buz_tim.duty(0)
    utime.sleep_ms(int(msec * 0.1))


async def play_song(song):
    tune = RTTTL(songs.find(song))
    for freq, msec in tune.notes():
        await play_tone(freq, msec)
        if not door_state.is_open:
            return

