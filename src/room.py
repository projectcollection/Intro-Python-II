# Implement a class to hold room information. This should have name and
# description attributes.
from items import Item

class Room():
	
	def __init__(self, name, desc, items = []):
		self.name = name
		self.desc = desc
		self.n_to = None
		self.s_to = None
		self.e_to = None
		self.w_to = None
		self.items = []

		for item in items:
			if(isinstance(item, Item)):
				self.items.append(item)

	def __str__(self):
		return f"{self.name} \n {self.desc}"
		
	def get_item(self, item_name, get_all = False):
		items = [item for item in self.items if item.name == item_name]
		if len(items) == 0:
			return []
		elif get_all:
			for item in items:
				self.remove_item(item)
			return items
		else:
			self.remove_item(items[0])
			return [items[0]]

	def get_items(self):
		return self.items
	
	def add_item(self, item):
		if(isinstance(item, list)):
			for i in item:
				self.items.append(i)
		else:
			self.items.append(item)

	def remove_item(self, to_remove):
		for index, item in enumerate(self.items):
			if item.name == to_remove.name:
				del self.items[index]

	