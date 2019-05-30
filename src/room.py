# Implement a class to hold room information. This should have name and
# description attributes.
from carrier import Item_Carrier

class Room(Item_Carrier):
	
	def __init__(self, name, desc, items = []):
		self.desc = desc
		self.n_to = None
		self.s_to = None
		self.e_to = None
		self.w_to = None
		return super().__init__(name, items)

	def __str__(self):
		return f"{self.name} \n {self.desc}"