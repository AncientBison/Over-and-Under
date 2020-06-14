import random

class deck:
	def __init__(self):
		self.cards = []
		for i in range(1,5):
			for num in range(1,11):
				self.cards.append(num)
	random.shuffle(self.cards)
	def draw(self):
		return self.cards.pop(0)
d = deck