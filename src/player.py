# Write a class to hold player information, e.g. what room they are in
# currently.
from carrier import Item_Carrier

class Player(Item_Carrier):
	def __init__(self, name, current_loc, items = []):
		self.current_loc = current_loc
		return super().__init__(name, items)

	def move(self, new_room):
		self.current_loc = new_room