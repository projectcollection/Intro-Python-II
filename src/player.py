# Write a class to hold player information, e.g. what room they are in
# currently.
from carrier import Item_Carrier

class Player(Item_Carrier):
	def __init__(self, name, current_loc, items = []):
		self.current_loc = current_loc
		return super().__init__(name, items)

	def move(self, direction):
		newRoom = getattr(self.current_loc, f'{direction.lower()}_to')
		if(newRoom is not None):
			self.current_loc = new_room
		else:
			print(f'There\'s no room at {direction.upper()}')