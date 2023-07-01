import random #Allows generation of random numbers/choices
import os #Allows clearing of the terminal
import pickle #saving of the game

save_filename = 'game_state.pkl'

def save_game_state(current_room, player_health):
    game_state = {
        'current_room': current_room,
        'player_health': player_health,
        'items': current_room.items,
        'monster_health': [monster.health for monster in current_room.monsters]
    }

    with open(save_filename, 'wb') as save_file:
        pickle.dump(game_state, save_file)


def load_game_state():
    try:
        with open(save_filename, 'rb') as save_file:
            game_state = pickle.load(save_file)
        current_room = game_state['current_room']
        player_health = game_state['player_health']
        items = game_state['items']
        monster_health = game_state['monster_health']

        # Update the current room's items
        for item in items:
            current_room.add_item(item)

        # Update the monster health in the current room
        for i, monster in enumerate(current_room.monsters):
            monster.health = monster_health[i]

        return current_room, player_health
    except FileNotFoundError:
        return None, None



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
            print("Game over. You have died.")
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
    clear()
    
    if current_room is None or player_health is None:
        # Create rooms
        ug_cabin = Room("Underground Cabin", "A dark, dirty underground room.")
        ug_tunnel = Room("Underground Tunnel", "A dark, dirty underground tunnel.")
        landing_g = Room("Ground Floor Landing", "A small room with a coat hanger.")
        dining = Room("Dining Room", "A small room with a wooden table that has rotten food atop it.")
        dungeon = Room("Dungeon", "A dark, murky room. You can make out a dead skeleton.", locked=True)
        lounge = Room("Lounge", "A room with 2 armchairs and a log fire that went out long ago.")
        clothing = Room("Clothing Room", "A small storage room with clothes hung on the walls.", locked=True)
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
        lounge.adjacent_rooms = [landing_f1, clothing, bedroom,landing_f2]
        clothing.adjacent_rooms = [lounge, landing_f2]
        landing_f1.adjacent_rooms = [lounge, attic, clothing, dining]
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

        # create keys
        dungeon_key = Key("Dungeon Key", "A key that unlocks the dungeon", room_to_unlock=dungeon)

        # Create monsters
        goblin = Monster("Goblin", "A small and vicious creature.", 20, 5)
        dragon = Monster("Dragon", "A fire-breathing dragon!", 100, 20)

        # Add items and monsters to rooms
        ug_cabin.add_item([stone])
        ug_tunnel.add_item([flint])
        landing_g.add_item([sword])
        dining.add_item([dungeon_key])
        dungeon.add_item([])
        lounge.add_item([])
        clothing.add_item([])
        landing_f1.add_item([])
        landing_f2.add_item([])
        bedroom.add_item([])
        bathroom.add_item([])
        treasury.add_item([])
        chest_room.add_item([])
        attic.add_item([])

        ug_cabin.add_monster([dragon])
        ug_tunnel.add_monster([goblin])
        landing_g.add_monster([])
        dining.add_monster([])
        dungeon.add_monster([])
        lounge.add_monster([])
        clothing.add_monster([])
        landing_f1.add_monster([])
        landing_f2.add_monster([])
        bedroom.add_monster([])
        bathroom.add_monster([])
        treasury.add_monster([])
        chest_room.add_monster([])
        attic.add_monster([])

        current_room = landing_g
        player_health = 100

        clear()
    while True:
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
            else:
                print(f"{col.lightblue}{c}. {room.name}{col.reset}")
            c += 1

        print("\nWhat would you like to do?")
        print(col.grey + "1. Move to another room")
        print("2. Pick up an item")
        print("3. Attack a monster")
        print("4. View inventory")
        print("5. Use an item")
        print("6. Quit" + col.reset)
        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("Enter the number of the room you wish to go to: ", end="")
            room_choice = current_room.adjacent_rooms[int(input())-1]
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
            else:
                clear()
                print(col.red + "You can't go to that room.\n" + col.reset)

        elif choice == "2":
            if current_room.items != []:
                print("Enter the number of the item you want to pick up: ", end="")
                item_choice = current_room.items[int(input())-1]
                item_choice = item_choice.name
                clear()
                for item in current_room.items:
                    if item.name.lower() == item_choice.lower():
                        if item.name == "Poisonous Mushroom":
                            print("You picked up the Poisonous Mushroom. It harms you!")
                            player.take_damage(10)
                            print(f"You took 10 damage. Your health is now {player.health}.\n")
                        elif isinstance(item, Key):
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
            else:
                clear()
                print(col.red + "There are no items in this room.\n" + col.reset)

        elif choice == "3":
            damage_from_player = player.damage
            if len(current_room.monsters) > 0:
                #monster = random.choice(current_room.monsters)
                print('Enter the number of the monster you wish to attack: ', end="") 
                monster = current_room.monsters[int(input())-1]
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
            print("Inventory:")
            if len(player.inventory) > 0:
                for i, item in enumerate(player.inventory):
                    print(f"{i+1}. {item.name}")
                item_choice = input("Enter the number of the item you want to use: ")
                if item_choice.isdigit() and 1 <= int(item_choice) <= len(player.inventory):
                    item_index = int(item_choice) - 1
                    item = player.inventory[item_index]
                    # Add item usage logic here
                    print(f"You used the {item.name}.\n")
                    player.remove_item_from_inventory(item)
                else:
                    print(col.red + "Invalid item choice.\n" + col.reset)
            else:
                print(col.grey + "Inventory is empty.\n" + col.reset)

        elif choice == "6":
            clear()
            save_game_state(current_room, player.health)  # Save player health instead of player_health
            print(col.lightblue + "Game saved. Goodbye!")
            break

        else:
            clear()
            print(col.red + "Invalid choice. Please try again.\n" + col.reset)

        if player_health <= 0:
            print("Game over. You have died.")
            break

if __name__ == "__main__":
    player = Player(100)
    main(player)
