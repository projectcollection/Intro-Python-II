import textwrap

from player import Player
from room import Room
from items import *

#Make some items
samurai = Weapon('samurai', 10, 500, 100)

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [samurai]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [samurai]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [samurai]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [samurai]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [samurai]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('player1', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def tut():
    return (
            'm(move) direction(N,E,S,W)\n'
            'i(item) command(inv->"inventory", ir->"in room", get, drop)\n'
            'i get(or)drop item_name\n'
            )	
def get_rooms_around(room):
    return (f'N: {room.n_to}\n'
            f'E: {room.e_to}\n'
            f'S: {room.s_to}\n'
            f'W: {room.w_to}')

def change_room(player, direction):
    newRoom = getattr(player.current_loc, f'{direction.lower()}_to')
    if(newRoom is not None):
        player.move(newRoom)
    else:
        print(f'There\'s no room at {direction}')

def item_action(player, action, item = '', get_all = False):
    if(action == 'inv'):
        print([i.name for i in player.items])
    elif(action == 'ir'):
        print([i.name for i in player.current_loc.items])
    elif(action == 'drop'):
        print('ITEM DROPPED IN ROOM')
        items = player.get_item(item, get_all)
        if(len(items) > 0):
            player.current_loc.add_item(items)
        else:
            print('Item not in inventory')
    elif(action == 'get'):
        print('ITEM ADDED TO INVENTORY')
        items = player.current_loc.get_item(item, get_all)
        if(len(items) > 0):
            player.add_item(items)
        else:
            print('Item not found in room')

while True:
    print('\n')
    print(f'Current Location: {player1.current_loc.name}')
    print(textwrap.fill(player1.current_loc.desc, 25))
    print(('-----\n'
            f'{textwrap.dedent(get_rooms_around(player1.current_loc))}\n'
            '-----\n'))
    print('\n')
    user_cmd = input('what\'s the move? write "tut" for tutorial\n>>>').split()
    
    if user_cmd[0] == 'q':
        break
    elif(user_cmd[0] == 'm' and len(user_cmd) >= 2 and user_cmd[1] in ('N', 'E', 'S', 'W')):
        change_room(player1, user_cmd[1])
    elif(user_cmd[0] == 'i'):
        if len(user_cmd) == 2:
            item_action(player1, user_cmd[1])
        else:
            item_action(player1, user_cmd[1], user_cmd[2])
    elif(user_cmd[0] == 'tut'):
        print(tut())
    else:
        print('Unknown Command')

