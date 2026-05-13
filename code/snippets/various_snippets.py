from machine import Pin
import time
import random


# ------------------------
#      BUTTON SETUP
# ------------------------
plus_button = Pin(1, Pin.IN, Pin.PULL_UP)
minus_button = Pin(2, Pin.IN, Pin.PULL_UP)
next_button = Pin(3, Pin.IN, Pin.PULL_UP)


# ------------------------
#   BUTTON READ FUNCTION
# ------------------------
def wait_for_button():
    while True:
        if not plus_button.value():
            time.sleep(0.2)
            return "+"
        if not minus_button.value():
            time.sleep(0.2)
            return "-"
        if not next_button.value():
            time.sleep(0.2)
            return "n"


# ------------------------
# CHEST SYSTEM CONFIG
# ------------------------
CHEST_COSTS = [10, 30, 50, 80, 100]
UPGRADE_COSTS = [20, 50, 80, 120, 200]


def get_chest_cost(player):
    count = len(player["chests"])
    if count >= len(CHEST_COSTS):
        return CHEST_COSTS[-1]
    return CHEST_COSTS[count]


def get_upgrade_cost(level):
    if level >= len(UPGRADE_COSTS):
        return None
    return UPGRADE_COSTS[level]


# ------------------------
#      PLAYER SETUP
# ------------------------
def setup_players():
    player_count = 2

    print("Select number of players (2–5)")

    while True:
        print("Players:", player_count)
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
            "chests": {}
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
        return random.randint(1, 5)
    return 0


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

        print("Press NEXT to roll")
        while wait_for_button() != "n":
            pass

        roll = random.randint(1, 6)
        print("Rolled:", roll)

        # Move
        new_pos, passed_start = move_player(player["position"], roll)
        player["position"] = new_pos

        if passed_start:
            print("Passed Start! +15 dabloons")
            player["dabloons"] += 15

        print("Moved to tile", new_pos)

        # Treasure
        found = treasure_roll()
        if found > 0:
            print("Found", found, "dabloons!")
            player["dabloons"] += found
        else:
            print("No treasure found")

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
                else:
                    print("Not enough dabloons")

        # ------------------------
        # OWN ISLAND - UPGRADE CHEST
        # ------------------------
        elif owner_name == player_name:
            chest = player["chests"][new_pos]
            level = chest["level"]

            upgrade_cost = get_upgrade_cost(level)

            if upgrade_cost is None:
                print("Chest already max level!")
            else:
                print("Upgrade chest? Cost:", upgrade_cost, "(+ yes / - no)")
                button = wait_for_button()

                if button == "+":
                    if player["dabloons"] >= upgrade_cost:
                        player["dabloons"] -= upgrade_cost
                        chest["level"] += 1
                        print("Chest upgraded to level", chest["level"])
                    else:
                        print("Not enough dabloons")

        # ------------------------
        # OTHER PLAYER OWNERSHIP (placeholder)
        # ------------------------
        else:
            print("Island owned by", owner_name)
            # (Rent + stealing logic to be added)

        # ------------------------
        #        END TURN
        # ------------------------
        print("Press NEXT to end turn")
        while wait_for_button() != "n":
            pass

        current_player_index = (current_player_index + 1) % len(turn_order)


# ------------------------
#       START GAME
# ------------------------
players = setup_players()
game_loop(players)