
class Card(object):
	
	def __init__(self,seed,name):
		self.seed = seed
		self.name = name

	def display_name(self):
		return self.name + " of " + self.seed

	def value(self):
		if (self.name == '2'):
			return (2,0)
		elif (self.name == '3'):
			return (3,0)
		elif (self.name == '4'):
			return (4,0)
		elif (self.name == '5'):
			return (5,0)
		elif (self.name == '6'):
			return (6,0)
		elif (self.name == '7'):
			return (7,0)
		elif (self.name == '8'):
			return (8,0)
		elif (self.name == '9'):
			return (9,0)
		elif (self.name == 'King'):
			return (10,0)
		elif (self.name == 'Queen'):
			return (10,0)
		elif (self.name == 'Jack'):
			return (10,0)
		elif (self.name == 'Ace'):
			return (11,1)
		else:
			return (0,0)


Seeds = ['Spades','Hearts','Diamonds','Clubs']

Card_types = ['2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace']

Deck = []

for seed in Seeds:
	for card_type in Card_types:
		Deck.append(Card(seed,card_type))

for card in Deck:
	print("Card = %s value = %d" %(card.display_name(), card.value()[0]))




