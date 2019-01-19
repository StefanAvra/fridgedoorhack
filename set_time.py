import ntptime
import uasyncio

# todo: implement check if online
# todo: turn wifi off after ntp sync and just go online when syncing


async def keep_time_synced():
    # From http://docs.micropython.org:
    # RTC in ESP8266 has very bad accuracy, drift may be seconds per minute.
    # Due to limitations of the ESP8266 chip the internal real-time clock (RTC) will overflow every 7:45h.
    while True:
        ntptime.settime()
        await uasyncio.sleep(3600)
