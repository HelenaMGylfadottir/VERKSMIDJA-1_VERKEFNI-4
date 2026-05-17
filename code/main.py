from machine import Pin, SoftI2C, PWM
import neopixel
from I2C_LCD import I2cLcd
from time import sleep, sleep_ms, ticks_ms, ticks_diff
import random

# ------------------------
# SPEAKER SETUP
# ------------------------
speaker = PWM(Pin(17))
speaker.duty(0)

# ------------------------
#      BUTTON SETUP
# ------------------------
plus_button = Pin(9, Pin.IN, Pin.PULL_UP)
minus_button = Pin(10, Pin.IN, Pin.PULL_UP)
next_button = Pin(11, Pin.IN, Pin.PULL_UP)

# -- Game button led's --
plus_Led = Pin(14, Pin.OUT)
minus_Led = Pin(21, Pin.OUT)
next_Led = Pin(12, Pin.OUT)

# ------------------------
# BASIC SOUND FUNCTIONS
# ------------------------
def play_tone(freq, duration_ms):
    speaker.freq(freq)
    speaker.duty(512)
    sleep_ms(duration_ms)
    speaker.duty(0)
    sleep_ms(50)


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

# ------------------------
#    REED SWITCH SETUP
# ------------------------
event_1 = Pin(4, Pin.IN, Pin.PULL_UP) # tile 6
event_2 = Pin(5, Pin.IN, Pin.PULL_UP) # tile 11
event_3 = Pin(6, Pin.IN, Pin.PULL_UP) # tile 16

start_tile = Pin(7, Pin.IN, Pin.PULL_UP) # tile 1

endSwitch = Pin(7, Pin.IN, Pin.PULL_UP)

# ------------------------
#    TILE SENSOR CHECK
# ------------------------
def is_event_tile(position):
    if position == 6:
        return True
    if position == 11:
        return True
    if position == 16:
        return True
    return False


def is_start_tile(position):
    return position == 1 and not start_tile.value()

# ------------------------
#       EVENT CARDS
# ------------------------
def trigger_event(player, position):
    while True:
        if not event_1.value():
            sleep(0.2)
            break
        if not event_2.value():
            sleep(0.2)
            break
        if not event_3.value():
            sleep(0.2)
            break
    
    print("Event tile!")
    lcd.clear()
    # Færi bendilinn í staf nr. 0 og línu nr. 0
    lcd.move_to(0, 0)
    lcd.putstr("Event tile!")
    sound_event()
    sleep(1)
    
    np.fill(off)
    np.write()
    sleep_ms(100)
    np.fill(white)
    np.write()
    sleep_ms(100)
    np.fill(off)
    np.write()
    sleep_ms(100)
    np.fill(white)
    np.write()
    sleep_ms(100)
    np.fill(off)
    np.write()
    sleep_ms(100)
    np.fill(white)
    np.write()
    sleep_ms(100)
    np.fill(off)
    np.write()
    
    sleep(1)

    choice = random.randint(1, 2)

    if choice == 1:
        print("Buried Booty!")
        
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr("Buried Booty!")
        sleep(1)
        
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr("Select number")
        sleep(1)
        
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr("You uncoverr")
        # Færi bendilinn í staf nr. 0 og línu nr. 1
        lcd.move_to(0, 1)
        lcd.putstr("hidden treasure!")
        sleep(1)
        
        print("+10 dabloons")
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr("+10 dabloons")
        sleep(1)
        
        player["dabloons"] += 10

    else:
        print("Stormy Seas!")
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr("Stormy Seas!")
        sleep(1)
        
        print("A violent storm scatters your loot!")
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr("A violent storm")
        # Færi bendilinn í staf nr. 0 og línu nr. 1
        lcd.move_to(0, 1)
        lcd.putstr("satters your loot!")
        sleep(1)
        
        print("-5 dabloons")
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr("-5 dabloons")
        sleep(1)
        
        player["dabloons"] -= 5
        if player["dabloons"] < 0:
            player["dabloons"] = 0

# -- LED strip --

# pin 1 = data pin for led
pin = Pin(1, Pin.OUT)
np = neopixel.NeoPixel(pin,6)
brightness = 70
white = [brightness,brightness,brightness]
off = [0,0,0]

# -- LCD --

i2c = SoftI2C(scl=Pin(48), sda=Pin(47), freq=400000)
lcd = I2cLcd(i2c, 39, 2, 16)

lcd.clear()
# Færi bendilinn í staf nr. 0 og línu nr. 0
lcd.move_to(0, 0)
lcd.putstr(" - Purrate -")
# Færi bendilinn í staf nr. 0 og línu nr. 1
lcd.move_to(0, 1)
lcd.putstr(" - Plunder -")

np.fill(white)
np.write()

sleep(3)

lcd.clear()

np.fill(off)
np.write()


# ------------------------
#   BUTTON READ FUNCTION
# ------------------------
def wait_for_button():
    while True:
        if not plus_button.value():
            sleep(0.2)
            sound_plus()
            return "+"
        if not minus_button.value():
            sleep(0.2)
            sound_minus()
            return "-"
        if not next_button.value():
            sleep(0.2)
            sound_next()
            return "n"


# ------------------------
# CHEST SYSTEM CONFIG
# ------------------------
CHEST_COSTS = [10, 30, 50, 80, 100]
UPGRADE_COSTS = [20, 50, 80, 120, 200]

RENT_COSTS = [5, 10, 20, 60, 80]


def get_chest_cost(player):
    count = len(player["chests"])
    if count >= len(CHEST_COSTS):
        return CHEST_COSTS[-1]
    return CHEST_COSTS[count]


def get_chest_rent(chest):
    for x in range(len(RENT_COSTS)):
        if x+1 == chest["level"]:
            return RENT_COSTS[x]
# ------------------------
#      PLAYER SETUP
# ------------------------
def setup_players():
    player_count = 2
    
    lcd.clear()
    # Færi bendilinn í staf nr. 0 og línu nr. 0
    lcd.move_to(0, 0)
    lcd.putstr("Select number")
    # Færi bendilinn í staf nr. 0 og línu nr. 1
    lcd.move_to(0, 1)
    lcd.putstr("of players (2-5)")

    sleep(2)
    lcd.clear()
    
    while True:
        #Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(f"Players: {player_count}")
        button = wait_for_button()

        if button == "+" and player_count < 5:
            player_count += 1
        elif button == "-" and player_count > 2:
            player_count -= 1
        elif button == "n":
            break
        
    players = {}

    for i in range(1, player_count + 1):
        players[f"Player {i}"] = {
            "position": 1,
            "dabloons": 15,
            "chests": {},
            "prison": 0,
        }

    return players


# ------------------------
# MOVE PLAYER (LOOP BOARD)
# ------------------------
def move_player(position, roll):
    new_position = position + roll
    passed_start = False

    if new_position > 20:
        new_position = new_position % 20
        if new_position == 0:
            new_position = 20
        passed_start = True

    return new_position, passed_start

# ------------------------
#    TREASURE SYSTEM
# ------------------------
def treasure_roll():
    if random.random() <= 0.4:
        nr = random.randint(1, 5)
        
        np.fill(white)
        np.write()
        sleep_ms(300)
        np.fill(off)
        np.write()
        sleep_ms(300)
        np.fill(white)
        np.write()
        sleep_ms(300)
        np.fill(off)
        np.write()
        sleep_ms(300)
        np.fill(white)
        np.write()
        sleep_ms(300)
        np.fill(off)
        np.write()
        sleep_ms(300)
        
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr("You found")
        # Færi bendilinn í staf nr. 0 og línu nr. 1
        lcd.move_to(0, 1)
        lcd.putstr(f"treasure! {nr}")
        return nr
    return 0

def dice_roll():
    spins = random.randint(5,10) # how often the led dice should spin
    nr = random.randint(1,6) # the random number it lands on
    velocity = 50
    damp = round(velocity / spins)
    while spins > 0: # spins the amount of times of spins
        for x in range(6):
            np.fill(off)
            np.write()
            np[x] = white
            np.write()
            sleep_ms(velocity)
        velocity += damp
        spins -= 1
    
    # -- led dice --
    np.fill(off)
    np.write()
    np[nr-1] = white
    np.write()
    
    
    lcd.clear()
    # Færi bendilinn í staf nr. 0 og línu nr. 0
    lcd.move_to(0, 0)
    lcd.putstr(f"Rolled {nr}")
    sleep(2)
    
    # -- lcd display --
    np.fill(off)
    np.write()
    #return nr
    return 1

sound_startup()

# ------------------------
#     MAIN GAME LOOP
# ------------------------
def game_loop(players):
    turn_order = list(players.keys())
    current_player_index = 0

    while True:
        player_name = turn_order[current_player_index]
        player = players[player_name]

        print()
        print("---", player_name, "TURN ---")
        print("Position:", player["position"], "| Dabloons:", player["dabloons"])
        
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr(f"{player_name} TURN")
        # Færi bendilinn í staf nr. 0 og línu nr. 1
        lcd.move_to(0, 1)
        lcd.putstr(f"Pos:{player["position"]} $:{player["dabloons"]}")
        
        if player["prison"] == 0:
        
            while wait_for_button() != "n":
                pass

            roll = dice_roll()
            lcd.clear()
            

            # Move
            new_pos, passed_start = move_player(player["position"], roll)
            player["position"] = new_pos

            if passed_start:
                print("Passed Start! +15 dabloons")
                
                lcd.clear()
                # Færi bendilinn í staf nr. 0 og línu nr. 0
                lcd.move_to(0, 0)
                lcd.putstr("Passed Start!")
                # Færi bendilinn í staf nr. 0 og línu nr. 1
                lcd.move_to(0, 1)
                lcd.putstr("+15 dabloons")
                
                player["dabloons"] += 15

            print("Moved to tile", new_pos)
            
            lcd.clear()
            # Færi bendilinn í staf nr. 0 og línu nr. 0
            lcd.move_to(0, 0)
            lcd.putstr(f"Moved to tile {new_pos}")
            sleep(1.5)
            
            if is_event_tile(new_pos) != True:
            
                # Treasure
                found = treasure_roll()
                if found > 0:
                    print("Found", found, "dabloons!")
                    
                    lcd.clear()
                    # Færi bendilinn í staf nr. 0 og línu nr. 0
                    lcd.move_to(0, 0)
                    lcd.putstr("You found")
                    # Færi bendilinn í staf nr. 0 og línu nr. 1
                    lcd.move_to(0, 1)
                    lcd.putstr(f"{found} dabloons!")
                    sound_found_dabloons()
                    sleep(1.5)
                    
                    player["dabloons"] += found
                else:
                    sound_no_dabloons()
                    print("No treasure found")
                    lcd.clear()
                    # Færi bendilinn í staf nr. 0 og línu nr. 0
                    lcd.move_to(0, 0)
                    lcd.putstr("No treasure")
                    # Færi bendilinn í staf nr. 0 og línu nr. 1
                    lcd.move_to(0, 1)
                    lcd.putstr("found")
                    sound_found_dabloons()
                    sleep(1.5)

                # ------------------------
                #     CHECK OWNERSHIP
                # ------------------------
                owner_name = None
                for name, p in players.items():
                    if new_pos in p["chests"]:
                        owner_name = name
                        break

                # ------------------------
                # EMPTY ISLAND - BUY CHEST
                # ------------------------
                if owner_name is None:
                    
                    print("Empty island. Place chest? (+ yes / - no)")
                    
                    lcd.clear()
                    # Færi bendilinn í staf nr. 0 og línu nr. 0
                    lcd.move_to(0, 0)
                    lcd.putstr("Empty island | y")
                    # Færi bendilinn í staf nr. 0 og línu nr. 1
                    lcd.move_to(0, 1)
                    lcd.putstr("Place chest? | n")
                    
                    button = wait_for_button()

                    if button == "+":
                        cost = get_chest_cost(player)
                        
                        print("Chest cost:", cost)

                        if player["dabloons"] >= cost:
                            player["dabloons"] -= cost
                            player["chests"][new_pos] = {
                                "level": 1,
                                "stored": 0
                            }
                            print("Chest placed!")
                            
                            lcd.clear()
                            # Færi bendilinn í staf nr. 0 og línu nr. 0
                            lcd.move_to(0, 0)
                            lcd.putstr("Chest placed!")
                            sleep(1.5)
                            
                        else:
                            print("Not enough dabloons")
                            
                            lcd.clear()
                            # Færi bendilinn í staf nr. 0 og línu nr. 0
                            lcd.move_to(0, 0)
                            lcd.putstr("Not enough")
                            # Færi bendilinn í staf nr. 0 og línu nr. 1
                            lcd.move_to(0, 1)
                            lcd.putstr("dabloons")

                # ------------------------
                # OWN ISLAND - UPGRADE CHEST - INSERT MONEY
                # ------------------------
                elif owner_name == player_name:
                    chest = player["chests"][new_pos]
                    level = chest["level"]
                    
                    lcd.clear()
                    # Færi bendilinn í staf nr. 0 og línu nr. 0
                    lcd.move_to(0, 0)
                    lcd.putstr("Your Island")
                    sound_own_island()
                    sleep(1)
                    
                    lcd.clear()
                    # Færi bendilinn í staf nr. 0 og línu nr. 0
                    lcd.move_to(0, 0)
                    lcd.putstr("UPGRADE      | y")
                    # Færi bendilinn í staf nr. 0 og línu nr. 1
                    lcd.move_to(0, 1)
                    lcd.putstr("INSTERT      | n")
                
                    button = wait_for_button()
                    
                    if button == "+":
                        upgrade_cost = GET_UPGRADE_COST(level)

                        if upgrade_cost is None:
                            print("Chest already max level!")
                            
                            lcd.clear()
                            # Færi bendilinn í staf nr. 0 og línu nr. 0
                            lcd.move_to(0, 0)
                            lcd.putstr("Chest already")
                            # Færi bendilinn í staf nr. 0 og línu nr. 1
                            lcd.move_to(0, 1)
                            lcd.putstr("max level!")
                        else:
                            print("Upgrade chest? Cost:", upgrade_cost, "(+ yes / - no)")
                            lcd.clear()
                            # Færi bendilinn í staf nr. 0 og línu nr. 0
                            lcd.move_to(0, 0)
                            lcd.putstr("Upgrade cost | y")
                            # Færi bendilinn í staf nr. 0 og línu nr. 1
                            lcd.move_to(0, 1)
                            lcd.putstr(f"{upgrade_cost}$ Dabloons  | n")
                            button = wait_for_button()

                            if button == "+":
                                if player["dabloons"] >= upgrade_cost:
                                    player["dabloons"] -= upgrade_cost
                                    chest["level"] += 1
                                    print("Chest upgraded to level", chest["level"])
                                else:
                                    print("Not enough dabloons")
                            else:
                                pass
                    elif button == "-":
                        while True:
                            button = wait_for_button()
                            money_count = 0
                            if button == "+" and player_count < 5:
                                money_count += 1
                            elif button == "-" and player_count > 2:
                                money_count -= 1
                            elif button == "n":
                                break
                        player["dabloons"] -= money_count
                        player["chests"][new_pos]
                    

                # ------------------------
                # OTHER PLAYER OWNERSHIP (placeholder)
                # ------------------------
                else:
                    sound_enemy_island()
                    print("Island owned by", owner_name)
                    lcd.clear()
                    # Færi bendilinn í staf nr. 0 og línu nr. 0
                    lcd.move_to(0, 0)
                    lcd.putstr(f"{owner_name}'s Island")
                    sleep(1.5)
                    
                    lcd.clear()
                    # Færi bendilinn í staf nr. 0 og línu nr. 0
                    lcd.move_to(0, 0)
                    lcd.putstr(f"Rent from {owner_name}")
                    # Færi bendilinn í staf nr. 0 og línu nr. 1
                    lcd.move_to(0, 1)
                    lcd.putstr(f"{get_chest_rent(owner_name["chests"][new_pos])}")
                    sleep(3)
                    
                    if player["dabloons"] >= get_chest_rent(owner_name["chests"][new_pos]):
                        player["dabloons"] -= get_chest_rent(owner_name["chests"][new_pos])
                        
                        lcd.clear()
                        # Færi bendilinn í staf nr. 0 og línu nr. 0
                        lcd.move_to(0, 0)
                        lcd.putstr("You have")
                        # Færi bendilinn í staf nr. 0 og línu nr. 1
                        lcd.move_to(0, 1)
                        lcd.putstr(f"{player["dabloons"] - get_chest_rent(owner_name["chests"][player["position"]])} left ")
                        sleep(1.5)
                    else:
                        player["prison"] = 2
                        lcd.clear()
                        # Færi bendilinn í staf nr. 0 og línu nr. 0
                        lcd.move_to(0, 0)
                        lcd.putstr("Dont have enough")
                        # Færi bendilinn í staf nr. 0 og línu nr. 1
                        lcd.move_to(0, 1)
                        lcd.putstr("Go to prison")
                        sleep(1.5)
            else:
                trigger_event(player, new_pos)
        else:
            player["prison"] -= 1
            lcd.clear()
            # Færi bendilinn í staf nr. 0 og línu nr. 0
            lcd.move_to(0, 0)
            lcd.putstr("Still in prison")
            # Færi bendilinn í staf nr. 0 og línu nr. 1
            lcd.move_to(0, 1)
            lcd.putstr("1 more turn")

        # ------------------------
        #        END TURN
        # ------------------------
        print("Press NEXT to end turn")
        lcd.clear()
        # Færi bendilinn í staf nr. 0 og línu nr. 0
        lcd.move_to(0, 0)
        lcd.putstr("Press NEXT")
        # Færi bendilinn í staf nr. 0 og línu nr. 1
        lcd.move_to(0, 1)
        lcd.putstr("to end turn")
        while wait_for_button() != "n":
            pass

        current_player_index = (current_player_index + 1) % len(turn_order)
        
# ------------------------
#       START GAME
# ------------------------
players = setup_players()
game_loop(players)

