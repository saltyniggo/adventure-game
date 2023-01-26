#work in progress text based adventure game
#shall evolve as time passes

#startup message
print('Welcome to T.B.A.G.!')
print('')
oida
#global variables
current_room = 'outside'
inventory = []

#room descriptions
rooms = {
    "outside": "You are outside a small cottage. There is a door to the east and a path to the south.",
    "inside": "You are inside the cottage. There is a table with a key on it, and a door to the west.",
    "inside_keyless": "You are inside the cottage. There is a door to the west.",
    "graveyard": "You are in a gloomy graveyard. There is a gate and the way back north."
}

#create the loop
while True:
    #tell in which room you are
    print(rooms[current_room])

    #ask for the user input
    print('What would you like to do?')
    action = input('')

    #different player actions
    if action == "go east" and current_room == "outside":
        print('You go east and step inside the little cottage.')
        current_room = "inside"
    elif action == "go west" and current_room == "inside":
        current_room = "outside"
    elif action == "go west" and current_room == "inside_keyless":
        current_room = "outside"
    elif action == "go south" and current_room == "outside":
        current_room = "graveyard"
    elif action == "go north" and current_room == "graveyard":
        current_room = "outside"
    elif action == "take key" and current_room == "inside":
        inventory.append("key")
        print("You have taken the key.")
        current_room = "inside_keyless"
    elif action == "open gate" and current_room == "graveyard":
        if "key" in inventory:
            print("You have unlocked the gate and won the game!")
            break
        else:
            print("The gate is locked. You need a key to open it.")
    else:
        print("I don't understand that command.")
