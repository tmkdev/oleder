import time

from board import SCL, SDA
import busio
import adafruit_ssd1306

from screens.stats import Stats
from screens.dtime import Dtime
from screens.analogclock import AnalogClock
from screens.logdir import LogDir
from screens.shutdown import Shutdown

from gpiozero import Button

running=True

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

stats = Stats(disp.width, disp.height)
dt = Dtime(disp.width, disp.height)
ac = AnalogClock(disp.width, disp.height)
ld = LogDir(disp.width, disp.height)
sd = Shutdown(disp.width, disp.height)

def call_shutdown():
    global running
    running=False

    sd.update(disp)

mods = [stats, ld, ac, dt, ]

shutdown = Button(21)

shutdown.when_held = call_shutdown

while running:
    for m in mods:
        for x in range(10):
            m.update(disp)
            time.sleep(1)

