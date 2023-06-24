import random #Allows generation of random numbers/choices
import os #Allows clearing of the terminal

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
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.monsters = []
        self.adjacent_rooms = []

    def add_item(self, item):
        self.items.append(item)

    def add_monster(self, monster):
        self.monsters.append(monster)

    def remove_item(self, item):
        self.items.remove(item)

    def remove_monster(self, monster):
        self.monsters.remove(monster)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Monster:
    def __init__(self, name, description, health, damage):
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage

def clear():
    os.system('cls||clear')

def main():
    # Create rooms
    dungeon = Room("Dungeon", "You are in a dark room. The smell of something vile fills your nostrils.")
    hall = Room("Hall", "You enter a large hall. The walls are damp and peeling.")
    corridor = Room("Corridor", "You find yourself in a narrow corridor. There are cobwebs almost everywhere you look.")

    # Define Adjacent Rooms
    dungeon.adjacent_rooms = [hall,corridor]
    hall.adjacent_rooms = [dungeon]
    corridor.adjacent_rooms = [dungeon]

    # Create items
    key = Item("Key", "A rusty old key.")
    sword = Item("Sword", "A sharp sword.")

    # Create monsters
    goblin = Monster("Goblin", "A small and vicious creature.", 20, 5)
    dragon = Monster("Dragon", "A fire-breathing dragon!", 100, 20)

    # Add items and monsters to rooms
    dungeon.add_item(key)
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
            print(col.lightblue + i.name + col.reset)

        print("\nWhat would you like to do?")
        print(col.grey + "1. Move to another room")
        print("2. Pick up an item")
        print("3. Attack a monster")
        print("4. Quit" + col.reset)
        choice = input("\nEnter your choice: ")

        if choice == "1":
            room_choice = input("Enter the name of the room you wish to go to: ")
            for i in rooms:
                if i.name.lower() == room_choice.lower():
                    current_room = i
                    clear()
                    break
            else:
                clear()
                print(col.red + "You can't go to that room." + col.reset)


        elif choice == "2":
            item_choice = input("Enter the name of the item you want to pick up: ")
            clear()
            for item in current_room.items:
                if item.name.lower() == item_choice.lower():
                    current_room.remove_item(item)
                    print(f"You picked up the {item.name}.")
                    break
            else:
                clear()
                print(col.red + "That item is not in the room." + col.reset)

        elif choice == "3":
            clear()
            if len(current_room.monsters) > 0:
                monster = random.choice(current_room.monsters)
                print(f"You attack the {monster.name}!")
                monster.health -= random.randint(10, 20)
                if monster.health <= 0:
                    print(f"You defeated the {monster.name}!")
                    current_room.remove_monster(monster)
                else:
                    print(f"The {monster.name} has {monster.health} health remaining.")
            else:
                print(col.red + "There are no monsters in the room." + col.reset)

        elif choice == "4":
            clear()
            print(col.lightblue + "Goodbye!")
            break
        else:
            clear()
            print(col.red + "Invalid choice. Please try again." + col.reset)

        if player_health <= 0:
            print("Game over. You have died.")
            break

if __name__ == "__main__":
    main()
