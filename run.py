import random

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

    while True:
        print(f"\n{current_room.name}")
        print(current_room.description)
        print("Items in the room:")
        for item in current_room.items:
            print(item.name)
        print("Monsters in the room:")
        for monster in current_room.monsters:
            print(monster.name)
        print("\nWhat would you like to do?")
        print("1. Move to another room")
        print("2. Pick up an item")
        print("3. Attack a monster")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            rooms = current_room.adjacent_rooms
            for i in rooms:
                print(i)

        elif choice == "2":
            item_choice = input("Enter the name of the item you want to pick up: ")
            for item in current_room.items:
                if item.name.lower() == item_choice.lower():
                    current_room.remove_item(item)
                    print(f"You picked up the {item.name}.")
                    break
            else:
                print("That item is not in the room.")
        elif choice == "3":
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
                print("There are no monsters in the room.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        if player_health <= 0:
            print("Game over. You have died.")
            break

if __name__ == "__main__":
    main()
