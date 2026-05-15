# ------------------------
#    REED SWITCH SETUP
# ------------------------
event_1 = Pin(4, Pin.IN, Pin.PULL_UP) # tile 6
event_2 = Pin(5, Pin.IN, Pin.PULL_UP) # tile 11
event_3 = Pin(6, Pin.IN, Pin.PULL_UP) # tile 16

start_tile = Pin(7, Pin.IN, Pin.PULL_UP) # tile 1

# ------------------------
#    TILE SENSOR CHECK
# ------------------------
def is_event_tile(position):
    if position == 6 and not event_1.value():
        return True
    if position == 11 and not event_2.value():
        return True
    if position == 16 and not event_3.value():
        return True
    return False


def is_start_tile(position):
    return position == 1 and not start_tile.value()

# ------------------------
#       EVENT CARDS
# ------------------------
def trigger_event(player):
    print("Event tile!")

    choice = random.randint(1, 2)

    if choice == 1:
        print("Buried Booty!")
        print("You uncover hidden treasure!")
        print("+10 dabloons")
        player["dabloons"] += 10

    else:
        print("Stormy Seas!")
        print("A violent storm scatters your loot!")
        print("-5 dabloons")
        player["dabloons"] -= 5
        if player["dabloons"] < 0:
            player["dabloons"] = 0