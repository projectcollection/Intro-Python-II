class Item():
	def __init__(self, name, weight, value):
		self.name = name
		self.weight = weight
		self.value = value

class Utility(Item):
	def __init__(self, name, weight, uses, value):
		self.uses = uses
		return super().__init__(name, weight, value)

class Weapon(Item):
	def __init__(self, name, weight, dmg, value):
		self.dmg = dmg
		return super().__init__(name, weight, value)