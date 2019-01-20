# fridgedoorhack
This is supposed to fix the issue with the door of the fridge in our flat.

### Issue
*tl;dr:* Door is left open unintentionally.

If you don't pay attention to close the fridge door properly, like when you push the door slightly in the hope that it's
going to close like a proper fridge would, it stays a cm or so open. This is partly due to the cracked door shelf and
partly due to the lack of attention. It's a cheap fridge but otherwise it's doing its job once it's closed properly. I
could buy a replacement shelf but that would be less fun (and more expensive).

### Solution
*tl;dr:* Check if door is longer open than it should be. If so, attract attention by playing RTTTL melodies. :notes:

I thought it would be nice if the fridge would play some melody if left open. So I added a buzzer to an ESP8266 and coded
the following project. I used `uasyncio` which is a port of Python's `asyncio` library for asynchronous code to
write coroutines that check for the door switch, play the RTTTL melodies, sync the time via ntp and write a log file when the
events are triggered.
At the time of writing this the latest stable version of MicroPython (v1.9.4) does not include all uasyncio modules,
thus I coded some workarounds. My code is not using the `aswitch.py` library nor is it cancelling tasks via `asyn.py`.

#### Audio
The ESP8266 does not have a built-in DAC. I wanted to keep it simple, so I thought a piezo buzzer is doing the job for now.
I used [dhylands' RTTTL Parser](https://github.com/dhylands/upy-rtttl) to play RTTTL coded songs.
[RTTTL ](https://en.wikipedia.org/wiki/Ring_Tone_Transfer_Language) is a ringtone
format developed by Nokia that was used to transfer ringtones to phones. You can simply find ringtones by searching 
`[song_name] rtttl`. But since the ESP8266 max PWM frequency is around 1kHz I had to modify the ringtones I wanted, to use lower frequencies.
Keep this in mind if you want to swap the ringtones.

## Getting Started
You can try this with your own fridge if you are interested.

### Prerequisites

#### Hardware:
* ESP8266 NodeMCU
* piezo buzzer
* a switch / button. I used metallic tape for the 'door switch'. 
* Power supply for your ESP8266. I used a phone charger.

#### Software:
The project is written in MicroPython, so I assume you have flashed the MicroPython firmware to your ESP8266 and set up your wifi connection.
I used v1.9.4, might work on other versions too.
Check the [official quick guide](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html) on how to get started with MicroPython.

### Installing
Get a local copy of this project with

```git clone https://github.com/StefanAvra/fridgedoorhack.git```

Copy the files to the ESP8266. I used [Adafruit's ampy](https://github.com/adafruit/ampy).
If you have ampy installed you can use the following code to copy all the needed files:

```
cd fridgedoorhack
ls *.py | xargs -n 1 ampy --port /dev/ttyUSB0 put
```

Reboot your MCU. It should sync the time via NTP. After that it starts checking your switch / door on pin 14 (D5).
Connect the piezo buzzer to pin 12 (D6) and ground. If the door opens the on-board LED (pin 2) will turn on.
Leaving the door open will play one of the ringtones after 20 seconds.

#### Config
You can modify a few settings in config.py.

```
BUTTON_PIN = 14  # pin for door switch
BUZZER_PIN = 12  # pin for piezo buzzer
ENABLE_LOG = True  # logs the events to log/door.log
LEGIT_OPEN_TIME = 20  # how many seconds until the alarm goes off
CLOSING_SOUND = True  # enable a confirmation sound for closing the door
ONE_UP = True  # play an achievement sound if the door was opened for COUNTER_MAX times
COUNTER_MAX = 100  # see above
```

## License
MIT License

Copyright (c) 2019 StefanAvra



rtttl.py is licensed under the MIT License by https://github.com/dhylands
