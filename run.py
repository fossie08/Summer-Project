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
        self.items.append(item)

    def add_monster(self, monster):
        self.monsters.append(monster)

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
        dungeon = Room("Dungeon", "You are in a dark room. The smell of something vile fills your nostrils.")
        hall = Room("Hall", "You enter a large hall. The walls are damp and peeling.")
        corridor = Room("Corridor", "You find yourself in a narrow corridor. There are cobwebs almost everywhere you look.", locked=True)

        # Define Adjacent Rooms
        dungeon.adjacent_rooms = [hall,corridor]
        hall.adjacent_rooms = [dungeon]
        corridor.adjacent_rooms = [dungeon]

        # Create items
        sword = Item("Sword", "A sharp sword.", 10)

        # create keys
        corridor_key = Key("Corridor Key", "A key that unlocks the corridor", room_to_unlock=corridor)

        # Create monsters
        goblin = Monster("Goblin", "A small and vicious creature.", 20, 5)
        dragon = Monster("Dragon", "A fire-breathing dragon!", 100, 20)

        # Add items and monsters to rooms
        hall.add_item(corridor_key)
        hall.add_item(sword)
        corridor.add_monster(goblin)
        corridor.add_monster(dragon)

        current_room = dungeon
        player_health = 100

        clear()
    while True:
        print(f"\n{current_room.name}")
        print(col.grey + current_room.description + col.reset)

        print("\nItems in the room:")
        for item in current_room.items:
            print(col.lightblue + item.name + col.reset)
        if current_room.items == []:
            print(col.grey + "None" + col.reset)

        print("\nMonsters in the room:")
        for monster in current_room.monsters:
            print(col.red + monster.name + col.reset)
        if current_room.monsters == []:
            print(col.grey + "None" + col.reset)

        rooms = current_room.adjacent_rooms
        print("\nRooms you can go to:" + col.reset)
        for i in rooms:
            if i.locked and not player.has_key(i):
                print(col.grey + i.name + col.red + " [Locked]" + col.reset)
            else:
                print(col.lightblue + i.name + col.reset)

        print("\nWhat would you like to do?")
        print(col.grey + "1. Move to another room")
        print("2. Pick up an item")
        print("3. Attack a monster")
        print("4. View inventory")
        print("5. Use an item")
        print("6. Quit" + col.reset)
        choice = input("\nEnter your choice: ")

        if choice == "1":
            room_choice = input("Enter the name of the room you wish to go to: ")
            for i in rooms:
                if i.name.lower() == room_choice.lower():
                    if i.locked and not player.has_key(i):
                        clear()
                        print(col.red + "The room is locked. You need a key to unlock it." + col.reset)
                        break
                    else:
                        current_room = i
                        clear()
                        break
            else:
                clear()
                print(col.red + "You can't go to that room." + col.reset)

        elif choice == "2":
            if current_room.items != []:
                item_choice = input("Enter the name of the item you want to pick up: ")
                clear()
                for item in current_room.items:
                    if item.name.lower() == item_choice.lower():
                        if item.name == "Poisonous Mushroom":
                            print("You picked up the Poisonous Mushroom. It harms you!")
                            player.take_damage(10)
                            print(f"You took 10 damage. Your health is now {player.health}.")
                        elif isinstance(item, Key):
                            player.add_key_to_inventory(item)
                            current_room.remove_item(item)
                            print(f"You picked up the {item.name}.")
                        else:
                            player.add_item_to_inventory(item)
                            current_room.remove_item(item)
                            print(f"You picked up the {item.name}.")
                        break
                else:
                    clear()
                    print(col.red + "That item is not in the room." + col.reset)
            else:
                clear()
                print(col.red + "There are no items in this room." + col.reset)

        elif choice == "3":
            damage_from_player = player.damage
            for i in player.inventory:
                damage_from_player += i.damage
            clear()
            if len(current_room.monsters) > 0:
                monster = random.choice(current_room.monsters)
                print(f"You attack the {monster.name}!")
                monster.health -= int(random.randint(75, 150) * damage_from_player / 100)
                if monster.health <= 0:
                    print(f"You defeated the {monster.name}!")
                    current_room.remove_monster(monster)
                else:
                    print(f"The {monster.name} has {col.red}{monster.health}{col.reset} health remaining.")
            else:
                print(col.red + "There are no monsters in the room." + col.reset)

        elif choice == "4":
            clear()
            print("Inventory:")
            if len(player.inventory) > 0:
                print("Items:")
                for item in player.inventory:
                    print(col.lightblue + item.name + col.reset)
            else:
                print(col.grey + "Empty" + col.reset)


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
                    print(f"You used the {item.name}.")
                    player.remove_item_from_inventory(item)
                else:
                    print(col.red + "Invalid item choice." + col.reset)
            else:
                print(col.grey + "Inventory is empty." + col.reset)

        elif choice == "6":
            clear()
            save_game_state(current_room, player.health)  # Save player health instead of player_health
            print(col.lightblue + "Game saved. Goodbye!")
            break

        else:
            clear()
            print(col.red + "Invalid choice. Please try again." + col.reset)

        if player_health <= 0:
            print("Game over. You have died.")
            break

if __name__ == "__main__":
    player = Player(100)
    main(player)
