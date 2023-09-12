import random #Allows generation of random numbers/choices
import os #Allows clearing of the terminal
import pickle #Allows saving of the game
import time #Allows waiting for certain periods of time

save_filename = 'game_state.pkl'
start_time = ''
def save_game_state(current_room, player_health):
    game_state = {
        'current_room': current_room,
        'player_health': player_health,
        #'items': current_room.items,
        'monster_health': [monster.health for monster in current_room.monsters],
        'inventory': player.inventory
    }

    with open(save_filename, 'wb') as save_file:
        pickle.dump(game_state, save_file)


def load_game_state():
    try:
        with open(save_filename, 'rb') as save_file:
            game_state = pickle.load(save_file)
        current_room = game_state['current_room']
        player_health = game_state['player_health']
        monster_health = game_state['monster_health']
        player.inventory = game_state['inventory']

        # Update the monster health in the current room
        for i, monster in enumerate(current_room.monsters):
            monster.health = monster_health[i]

        return current_room, player_health
    except FileNotFoundError:
        return None, 100



class col: #Allows formatting of text
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    grey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'


class Room:
    def __init__(self, name, description, locked=False):
        self.name = name
        self.description = description
        self.items = []
        self.monsters = []
        self.adjacent_rooms = []
        self.locked = locked

    def add_item(self, item):
        self.items = self.items + item

    def add_monster(self, monster):
        self.monsters = self.monsters + monster

    def remove_item(self, item):
        self.items.remove(item)

    def remove_monster(self, monster):
        self.monsters.remove(monster)

class Item:
    def __init__(self, name, description, damage=0):
        self.name = name
        self.description = description
        self.damage = damage

class Key(Item):
    def __init__(self, name, description, room_to_unlock):
        super().__init__(name, description) # Call the constructor of the superclass to initialize the 'name' and 'description' attributes

        self.room_to_unlock = room_to_unlock

    def unlock_room(self):
        self.room_to_unlock.locked = False

class Monster:
    def __init__(self, name, description, health, damage):
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage
        
class Player:
    def __init__(self, health):
        self.health = health
        self.inventory = []
        self.keys = []
        self.damage = 5

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            clear()
            print(f"{col.red}{col.bold}Game over. You have died.")
            # Additional actions or game over logic can be added here
            exit()

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def remove_item_from_inventory(self, item):
        self.inventory.remove(item)

    def add_key_to_inventory(self, key):
        self.keys.append(key)

    def has_key(self, room):
        for key in self.keys:
            if key.room_to_unlock == room:
                return True
        return False

def clear():
    os.system('cls||clear')

def main(player):
    current_room, player_health = load_game_state()
    player.health = player_health
    clear()
    
    if current_room is None or player_health is None:
        # Create rooms
        ug_cabin = Room("Underground Cabin", "A dark, dirty underground room.")
        ug_tunnel = Room("Underground Tunnel", "A dark, dirty underground tunnel.")
        landing_g = Room("Ground Floor Landing", "A small room with a coat hanger.")
        dining = Room("Dining Room", "A small room with a wooden table that has rotten food atop it.")
        dungeon = Room("Dungeon", "A dark, murky room. You can make out a dead skeleton.", locked=True)
        lounge = Room("Lounge", "A room with 2 armchairs and a log fire that went out long ago.")
        closet = Room("Closet", "A small storage room with clothes hung on the walls.", locked=True)
        landing_f1 = Room("First Floor Landing", "A small, dark room. a cat scurries away as you enter.")
        landing_f2 = Room("Second Floor Landing", "A cobweb-filled room with a broken chandelier.")
        bedroom = Room("Bedroom", "The master bedroom. a rotting woman is in the four-poster bed.", locked=True)
        bathroom = Room("Bathroom", "A small bathroom with a dripping tap.")
        treasury = Room("Treasury", "A small room with a small, locked chest.")
        chest_room = Room("Chest", "The small chest inside the treasury.", locked=True)
        attic = Room("Attic", "An old attic with a skeleton lying on a small table. a spider drops form the ceiling.")



        # Define Adjacent Rooms
        ug_cabin.adjacent_rooms = [ug_tunnel]
        ug_tunnel.adjacent_rooms = [ug_cabin, landing_g]
        landing_g.adjacent_rooms = [ug_tunnel, dining]
        dining.adjacent_rooms = [landing_g, dungeon, landing_f1]
        dungeon.adjacent_rooms = [dining]
        lounge.adjacent_rooms = [landing_f1, closet, bedroom,landing_f2]
        closet.adjacent_rooms = [lounge, landing_f2]
        landing_f1.adjacent_rooms = [lounge, attic, closet, dining]
        landing_f2.adjacent_rooms = [lounge,bedroom]
        bedroom.adjacent_rooms = [landing_f2, bathroom, lounge]
        bathroom.adjacent_rooms = [bedroom, attic]
        treasury.adjacent_rooms = [attic, chest_room]
        chest_room.adjacent_rooms = [treasury, attic]
        attic.adjacent_rooms = [landing_f1, bathroom, treasury]

        # Create items
        sword = Item("Sword", "A sharp sword.", 10)
        flint = Item("Flint", "A small, sharp piece of flint.", 5)
        stone = Item("Stone", "A medium-sized stone.", 3)
        bandage = Item("Bandage", "A roll of bandage")
        gold = Item("Gold", "A very shiny and very heavy ingot of gold", 15)
        gemstone = Item("Gemstone", "Lots of sparkling emerald-green gemstones", 1)

        # create keys
        dungeon_key = Key("Dungeon Key", "A large rusty key", room_to_unlock=dungeon)
        bedroom_key = Key("Bedroom Key", "A medium-sized steel key", room_to_unlock=bedroom)
        closet_key = Key("Closet Key", "A relatively small silver key", room_to_unlock=closet)
        chest_key = Key("Chest Key", "A very small golden key", room_to_unlock=chest_room)

        # Create monsters
        goblin = Monster("Goblin", "A small and vicious creature.", 20, 5)
        dragon = Monster("Dragon", "A fire-breathing dragon!", 100, 20)
        spider = Monster("Vicious Spider", "A vicious spider", 1, 3)
        ghoul = Monster("Ghoul", "An evil, haunting spirit", 1000, 3)
        skeleton = Monster("Skeleton", "A skeleton", 15, 7)
        living_gold = Monster("Living Gold", "Gold that has come to life", 10, 4)

        # Add items and monsters to rooms
        ug_cabin.add_item([stone])
        ug_tunnel.add_item([flint])
        landing_g.add_item([sword,bandage])
        dining.add_item([])
        dungeon.add_item([])
        lounge.add_item([bedroom_key])
        closet.add_item([chest_key])
        landing_f1.add_item([])
        landing_f2.add_item([closet_key])
        bedroom.add_item([bandage])
        bathroom.add_item([bandage])
        treasury.add_item([])
        chest_room.add_item([gold, gold, gemstone])
        attic.add_item([dungeon_key])

        ug_cabin.add_monster([dragon])
        ug_tunnel.add_monster([goblin])
        landing_g.add_monster([])
        dining.add_monster([ghoul, ghoul])
        dungeon.add_monster([spider, spider, skeleton, ghoul])
        lounge.add_monster([])
        closet.add_monster([ghoul])
        landing_f1.add_monster([ghoul])
        landing_f2.add_monster([spider])
        bedroom.add_monster([spider, spider])
        bathroom.add_monster([spider, spider])
        treasury.add_monster([living_gold])
        chest_room.add_monster([ghoul])
        attic.add_monster([spider, spider, spider])

        clear()
        current_room = chest_room
        start_time = time.time()
    while True:

        for item in player.inventory:
            if item.name == "Bandage":
                print(f"Your bandage heals you. It gives you {col.green}5{col.reset} health.")
                player.health += 5
                print(f"You now have {col.green}{player.health}{col.reset} health.\n")
                if random.randint(0,5) == 5:
                    print(f"{col.pink}Your bandage has run out!{col.reset}\n")
                    player.remove_item_from_inventory(item)
        
        damage_from_monsters = 0
        if current_room.monsters != []:
            for monster in current_room.monsters:
                damage_from_monsters += monster.damage
            if len(current_room.monsters) > 1:
                print("You are attacked by multiple monsters!")
            else:   
                print(f"You are attacked by a {monster.name}!")
            player.take_damage(int(random.randint(75, 150) * damage_from_monsters / 100))
            print(f"You have {col.red}{player.health}{col.reset} health remaining.\n")

        print(f"{current_room.name}")
        print(col.grey + current_room.description + col.reset)

        print("\nItems in the room:")
        c = 1
        for item in current_room.items:
            print(f"{col.lightblue}{c}. {item.name}{col.reset}")
            c += 1
        if current_room.items == []:
            print(col.grey + "None" + col.reset)

        print("\nMonsters in the room:")
        c = 1
        for monster in current_room.monsters:
            print(f"{col.red}{c}. {monster.name}{col.reset}")
            c += 1
        if current_room.monsters == []:
            print(col.grey + "None" + col.reset)

        rooms = current_room.adjacent_rooms
        print("\nRooms you can go to:" + col.reset)
        c = 1
        for room in rooms:
            if room.locked and not player.has_key(room):
                print(f"{col.grey}{c}. {room.name} {col.red}[Locked]{col.reset}")
            elif room.locked and player.has_key(room):
                print(f"{col.lightblue}{c}. {room.name} {col.green}[Unlocked]{col.reset}")
            elif room.name == 'Window':
                print(f"{col.lightblue}{c}. {room.name} {col.green}[EXIT]{col.reset}")
            else:
                print(f"{col.lightblue}{c}. {room.name}{col.reset}")
            c += 1

        # Display Options
        print("\nWhat would you like to do?")
        print(col.grey + "1. Move to another room")

        if int(len(current_room.items)) == 1:
            print("2. Pick up the item")
        else:
            print("2. Pick up an item")

        print("3. Attack a monster")
        print("4. View inventory")
        print("5. Close the program" + col.reset)

        if int(len(current_room.items)) == 0 and current_room.name == 'Chest':
            print(col.grey + "6. Jump out the window" + col.reset)
        choice = input("\nEnter your choice: ")

        # Interpret Input
        if choice == "1":
            room_choice = input("Enter the number of the room you wish to go to: ")

            try:
                current_room.adjacent_rooms[int(room_choice)-1]
            except:
                clear()
                print(f"{col.red}Invalid choice. Please try again.{col.reset}\n")
            else:

                room_choice = current_room.adjacent_rooms[int(room_choice)-1]
                room_choice = room_choice.name
                for i in rooms:
                    if i.name.lower() == room_choice.lower():
                        if i.locked and not player.has_key(i):
                            clear()
                            print(col.red + "The room is locked. You need a key to unlock it.\n" + col.reset)
                            break
                        else:
                            current_room = i
                            clear()
                            break

        elif choice == "2":
            if int(len(current_room.items)) > 1:
                item_choice = input("Enter the number of the item you want to pick up: ")

                try:
                    current_room.items[int(item_choice)-1]
                except:
                    clear()
                    print(f"{col.red}Invalid choice. Please try again.{col.reset}\n")
                else:

                    item_choice = current_room.items[int(item_choice)-1]
                    item_choice = item_choice.name
                    clear()
                    for item in current_room.items:
                        if item.name.lower() == item_choice.lower():
                            if isinstance(item, Key):
                                player.add_key_to_inventory(item)
                                current_room.remove_item(item)
                                print(f"You picked up the {item.name}.\n")
                            else:
                                player.add_item_to_inventory(item)
                                current_room.remove_item(item)
                                print(f"You picked up the {item.name}.\n")
                            break
                    else:
                        clear()
                        print(col.red + "That item is not in the room.\n" + col.reset)

            elif int(len(current_room.items)) == 1:
                clear()
                item = current_room.items[0]
                if isinstance(item, Key):
                    player.add_key_to_inventory(item)
                    current_room.remove_item(item)
                    print(f"You picked up the {item.name}.\n")
                else:
                    player.add_item_to_inventory(item)
                    current_room.remove_item(item)
                    print(f"You picked up the {item.name}.\n")

            else:
                clear()
                print(col.red + "There are no items in this room.\n" + col.reset)

        elif choice == "3":
            damage_from_player = player.damage
            for item in player.inventory:
                damage_from_player += item.damage

            if len(current_room.monsters) > 0:
                monster = input("Enter the number of the monster you wish to attack: ")

                try:
                    current_room.monsters[int(monster)-1]
                except:
                    clear()
                    print(f"{col.red}Invalid choice. Please try again.{col.reset}\n")
                else:

                    monster = current_room.monsters[int(monster)-1]
                    clear()
                    print(f"You attack the {monster.name}!")
                    monster.health -= int(random.randint(75, 150) * damage_from_player / 100)
                    if monster.health <= 0:
                        print(f"You defeated the {monster.name}!\n")
                        current_room.remove_monster(monster)
                    else:
                        print(f"The {monster.name} has {col.red}{monster.health}{col.reset} health remaining.\n")
                    
            else:
                clear()
                print(col.red + "There are no monsters in the room.\n" + col.reset)

        elif choice == "4":
            clear()
            print("Items:")
            if len(player.inventory) > 0:
                for item in player.inventory:
                    print(f"\n{col.lightblue}{item.name}{col.reset}")
                    print(f"{col.grey}{item.description}{col.reset}")
            else:
                print(col.grey + "Empty" + col.reset)

            print("\nKeys:")
            if len(player.keys) > 0:
                for key in player.keys:
                    print(f"\n{col.lightblue}{key.name}{col.reset}")
                    print(f"{col.grey}{key.description}{col.reset}")
            else:
                print(col.grey + "Empty" + col.reset)

            input("\nPress enter to continue...")
            clear()

        elif choice == "5":
            clear()
            save_game_state(current_room, player.health)  # Save player health instead of player_health
            print(col.lightblue + "Game saved. The program will close in 5 seconds.")
            time.sleep(5)
            break

        elif choice == "6" and int(len(current_room.items)) == 0 and current_room.name == 'Chest':
            stop_time = time.time()
            time_spent = round(stop_time - start_time,2)
            clear()
            print(col.green + col.bold + 'You have successfully escaped the dungeon and completed the game in',time_spent,'seconds!')
            print(col.reset + col.red + 'The game will close in 10 seconds.')
            time.sleep(10)
            clear()
            break

        else:
            clear()
            print(col.red + "Invalid choice. Please try again.\n" + col.reset)

if __name__ == "__main__":
    player = Player(100)
    main(player)