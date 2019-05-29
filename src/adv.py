import textwrap

from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
    print('\n\n')

while True:
    print(f'Current Location: {player1.current_loc.name}')
    print(textwrap.fill(player1.current_loc.desc, 25))
    print(('-----\n'
            f'{textwrap.dedent(get_rooms_around(player1.current_loc))}\n'
            '-----\n'))
    user_cmd = input('what\'s the move?\n>>>')
    
    if user_cmd == 'q':
        break
    elif(user_cmd in ('N', 'E', 'S', 'W')):
        change_room(player1, user_cmd)

