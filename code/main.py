from machine import Pin

# -- Game buttons --
upButton = Pin(9, Pin.IN, Pin.PULL_UP)
downButton = Pin(10, Pin.IN, Pin.PULL_UP)
enterButton = Pin(11, Pin.IN, Pin.PULL_UP)

# -- Game button led's --
upLed = Pin(14, Pin.OUT)
downLed = Pin(13, Pin.OUT)
enterLed = Pin(12, Pin.OUT)

# -- Reed switches --
event1 = Pin(4, Pin.IN, Pin.PULL_UP)
event2 = Pin(5, Pin.IN, Pin.PULL_UP)
event3 = Pin(6, Pin.IN, Pin.PULL_UP)

end = Pin(7, Pin.IN, Pin.PULL_UP)

# -- LCD and LED strip --
# pin 1 = data pin for led

# pin 47 = data pin 1 for lcd
# pin 48 = data pin 2 for lcd

while True:
    pass