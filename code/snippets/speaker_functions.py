from machine import Pin, PWM
import time

# ------------------------
# SPEAKER SETUP
# ------------------------
speaker = PWM(Pin(10))
speaker.duty(0)


# ------------------------
# BASIC SOUND FUNCTIONS
# ------------------------
def play_tone(freq, duration_ms):
    speaker.freq(freq)
    speaker.duty(512)
    time.sleep_ms(duration_ms)
    speaker.duty(0)
    time.sleep_ms(50)


def play_melody(notes):
    for freq, duration in notes:
        play_tone(freq, duration)


# ------------------------
# GAME START SOUND
# ------------------------
def sound_startup():
    melody = [
        (600, 100),
        (800, 100),
        (1000, 100),
        (1200, 100),
        (1000, 100),
        (1600, 200),
    ]
    play_melody(melody)


# ------------------------
# TREASURE SOUNDS
# ------------------------
def sound_found_dabloons():
    melody = [
        (800, 100),
        (1000, 100),
        (1300, 150),
    ]
    play_melody(melody)


def sound_no_dabloons():
    melody = [
        (600, 150),
        (400, 200),
    ]
    play_melody(melody)


# ------------------------
# ISLAND INTERACTION SOUNDS
# ------------------------
def sound_enemy_island():
    melody = [
        (500, 150),
        (650, 150),
        (500, 200),
    ]
    play_melody(melody)


def sound_own_island():
    melody = [
        (900, 100),
        (1100, 100),
        (1400, 200),
    ]
    play_melody(melody)


# ------------------------
# EVENT TILE SOUND
# ------------------------
def sound_event():
    melody = [
        (700, 100),
        (1200, 100),
        (900, 200),
    ]
    play_melody(melody)


# ------------------------
# BUTTON SOUNDS
# ------------------------
def sound_plus():
    play_tone(1000, 50)


def sound_minus():
    play_tone(500, 50)


def sound_next():
    play_tone(800, 50)
