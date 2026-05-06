from machine import Pin, SoftI2C
import neopixel
from I2C_LCD import I2cLcd
from time import sleep_ms


# -- Game buttons --
upButton = Pin(9, Pin.IN, Pin.PULL_UP)
downButton = Pin(10, Pin.IN, Pin.PULL_UP)
enterButton = Pin(11, Pin.IN, Pin.PULL_UP)

# -- button mechanics --
upButtonPrevStatus = 1
upButtonPressed = False


# -- Game button led's --
upLed = Pin(14, Pin.OUT)
downLed = Pin(13, Pin.OUT)
enterLed = Pin(12, Pin.OUT)

# -- Reed switches --
event1 = Pin(4, Pin.IN, Pin.PULL_UP)
event2 = Pin(5, Pin.IN, Pin.PULL_UP)
event3 = Pin(6, Pin.IN, Pin.PULL_UP)

endSwitch = Pin(7, Pin.IN, Pin.PULL_UP)

# -- LED strip --

# pin 1 = data pin for led
pin = Pin(1, Pin.OUT)
np = neopixel.NeoPixel(pin,6)
brightness = 200
white = [brightness,brightness,brightness]
off = [0,0,0]

# -- LCD --

i2c = SoftI2C(scl=Pin(48), sda=Pin(47), freq=400000)
lcd = I2cLcd(i2c, 39, 2, 16)

# Færi bendilinn í staf nr. 0 og línu nr. 0
lcd.move_to(0, 0)
lcd.putstr("Hallo")
# Færi bendilinn í staf nr. 0 og línu nr. 1
lcd.move_to(0, 1)
lcd.putstr("Heimur")

lcd.move_to(8,0)
lcd.putstr("BEEBEE")


# -- dice mechanic --
diceNr = 0
dice = False

while True:
    
    upButtonStatus = upButton.value()
    if upButtonStatus == 0 and upButtonPrevStatus == 1:
        upButtonPressed = not upButtonPressed
    upLed.value(upButtonPressed)
    upButtonStatus = upButtonStatus

    
    
    
    while dice == True:
        for x in range(6):
            diceNr = x+1
            np.fill(off)
            np.write()
            np[x] = white
            np.write()
            sleep_ms(50)