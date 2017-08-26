from random import randint


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


class Player(object):

	def __init__(self,name):
		self.name = name
		self.Cards = []
		self.HiddenCards = []

	def get_name(self):
		return self.name

	def add_card(self,card):
		self.Cards.append(card)

	def show_cards(self):
		for card in self.HiddenCards:
			print ("Hidden Card")

		for card in self.Cards:
			print (card.display_name())

	


class Dealer(Player):

	def __init__(self):
		Player.__init__(self, 'Dealer')

	def add_hidden_card(self,card):
		self.HiddenCards.append(card)



class OrdinaryPlayer(Player):
	
	def __init__(self,name,bankroll):
		Player.__init__(self,name)
		self.bankroll = bankroll

	def get_bankroll(self):
		return self.bankroll

	def increase_bankroll(self, amount):
		self.bankroll += amount

	def decrease_bankroll(self, amount):
		self.bankroll -= amount


Seeds = ['Spades','Hearts','Diamonds','Clubs']

Card_types = ['2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace']

Deck = []

for seed in Seeds:
	for card_type in Card_types:
		Deck.append(Card(seed,card_type))

#for card in Deck:
#	print("Card = %s value = %d" %(card.display_name(), card.value()[0]))


Players_name = ['Joe', 'Mark', 'Anna']

players = []

dealer = Dealer()

for player_name in  Players_name:
	players.append(OrdinaryPlayer(player_name,100))


dealer.add_card(Deck[randint(0, len(Deck))])
dealer.add_hidden_card(Deck[randint(0, len(Deck))])
print('Dealer:')
dealer.show_cards()

for player in players:
	player.add_card(Deck[randint(0, len(Deck))])
	player.add_card(Deck[randint(0, len(Deck))])
	print(player.get_name() + ':')
	player.show_cards()





