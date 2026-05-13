from machine import Pin, SoftI2C
import neopixel
from I2C_LCD import I2cLcd
from time import sleep_ms, ticks_ms, ticks_diff
import random


# -- Game buttons --
upButton = Pin(9, Pin.IN, Pin.PULL_UP)
downButton = Pin(10, Pin.IN, Pin.PULL_UP)
enterButton = Pin(11, Pin.IN, Pin.PULL_UP)

# -- button mechanics --
upButtonPrevStatus = 1
upButtonPressed = False

downButtonPrevStatus = 1
downButtonPressed = False

enterButtonPrevStatus = 1
enterButtonPressed = False

# -- Game button led's --
upLed = Pin(14, Pin.OUT)
downLed = Pin(21, Pin.OUT)
enterLed = Pin(12, Pin.OUT)

downLed.value(1)

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

sleep_ms(1000)

lcd.clear()

# -- dice mechanic --
dice = False

# -- round mechanic place holder --

square = "null"
startRound = True

while True:

    upButtonStatus = upButton.value()
    if upButtonStatus == 0 and upButtonPrevStatus == 1:
        upButtonPressed = not upButtonPressed
    upButtonStatus = upButtonStatus
    
    downButtonStatus = downButton.value()
    if downButtonStatus == 0 and downButtonPrevStatus == 1:
        downButtonPressed = not downButtonPressed
    downButtonStatus = downButtonStatus
    
    enterButtonStatus = enterButton.value()
    if enterButtonStatus == 0 and enterButtonPrevStatus == 1:
        enterButtonPressed = not enterButtonPressed
    enterButtonStatus = enterButtonStatus
    
    
    if enterButtonPressed == True:
        if startRound == True:
            dice = True
            enterButtonPressed = False
    
    if dice == True:
        
        # -- function --
        spins = random.randint(5,10) # how often the led dice should spin
        nr = random.randint(1,6) # the random number it lands on
        
        while spins > 0: # spins the amount of times of spins
            for x in range(6):
                np.fill(off)
                np.write()
                np[x] = white
                np.write()
                sleep_ms(50)
            spins -= 1
        
        # -- led dice --
        np.fill(off)
        np.write()
        np[nr-1] = white
        np.write()
        sleep_ms(400)
        
        # -- lcd display --
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Kastad teningur")
        lcd.move_to(0, 1)
        lcd.putstr(f"Tu fekst {nr}")
        sleep_ms(3000)
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Leikmadur x")
        lcd.move_to(0, 1)
        lcd.putstr("Faerdu a reit x")
        dice = False
    
    if square == "island":
        chosen = False
        while chosen == False
            sw_time = 400
            start_time = tics_ms()
            while ticks_diff(ticks_ms(),start_time) < sw_time:
                lcd.clear()
                lcd.move_to(0, 0)
                lcd.putstr("Eyja x")
                lcd.move_to(0, 1)
                lcd.putstr("Villtu kaupa?")
                
                upButtonStatus = upButton.value()
                if upButtonStatus == 0 and upButtonPrevStatus == 1:
                    upButtonPressed = not upButtonPressed
                upButtonStatus = upButtonStatus
                
                downButtonStatus = downButton.value()
                if downButtonStatus == 0 and downButtonPrevStatus == 1:
                    downButtonPressed = not downButtonPressed
                downButtonStatus = downButtonStatus
                
                if upButtonPressed == True:
                    chosen = True
                    upButtonPressed = False
                    players[x]["dabloons"] -= square[x]["price"]
                    players[x]["islands"].append(square[x]["nr"])
                
                elif downButtonPressed == True:
                    
                
            while ticks_diff(ticks_ms(),start_time) < sw_time:
                lcd.clear()
                lcd.move_to(0, 0)
                lcd.putstr("Kaupa")
                lcd.move_to(0, 1)
                lcd.putstr("Sleppa")

