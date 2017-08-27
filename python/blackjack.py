import random


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
		elif (self.name == '10'):
			return (10,0)
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

	def score(self):
		score = 0
		reduction = []

		for card in self.HiddenCards:
			value = card.value()
			score += value[0]
			if (value[1] != value[0] and value[1] != 0):
				reduction.append(value[0]-value[1])

		for card in self.Cards:
			value = card.value()
			score += value[0]
			if (value[1] != value[0] and value[1] != 0):
				reduction.append(value[0]-value[1])

		reduction.sort();
		#print(reduction)
		for red in reduction:
			if (score > 21):
				score -= red 
			


		return score

	

class Dealer(Player):

	def __init__(self):
		Player.__init__(self, 'Dealer')

	def add_hidden_card(self,card):
		self.HiddenCards.append(card)

	def reveal_cards(self):
		for card in self.HiddenCards:
			print (card.display_name())

		for card in self.Cards:
			print (card.display_name())


class OrdinaryPlayer(Player):
	
	def __init__(self,name,bankroll,bet):
		Player.__init__(self,name)
		self.bankroll = bankroll
		self.bet = bet
		self.busted = False
		self.BlackJack = False

	def get_bankroll(self):
		return self.bankroll

	def increase_bankroll(self, amount):
		self.bankroll += amount

	def decrease_bankroll(self, amount):
		self.bankroll -= amount

	def get_bet(self):
		return self.bet

	def set_bet(self,bet):
		self.bet = bet

	def set_status(self,busted,BlackJack):
		self.busted = busted
		self.BlackJack = BlackJack

	def get_busted(self):
		return self.busted

	def get_BlackJack(self):
		return self.BlackJack




Seeds = ['Spades','Hearts','Diamonds','Clubs']

Card_types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

Deck = []

def extract_card(Deck):
	try: 
		card = random.choice(Deck)
		Deck.remove(card)
		return card
	except:
		print("No more cards!")
		

for seed in Seeds:
	for card_type in Card_types:
		Deck.append(Card(seed,card_type))

Players_name = ['Joe', 'Mark', 'Anna', 'Robert']
#Players_name = ['Joe']

players = []

dealer = Dealer()

for player_name in  Players_name:
	players.append(OrdinaryPlayer(player_name,1000,10))


print("Initial cards:")
print("")
dealer.add_card(extract_card(Deck))
dealer.add_hidden_card(extract_card(Deck))
print('Dealer:')

dealer.show_cards()
#print("score = %d" %(dealer.score()))

for player in players:
	#player.add_card(extract_card(Deck))
	player.add_card(extract_card(Deck))
	player.add_card(extract_card(Deck))
	print("")
	print(player.get_name() + ':')
	player.show_cards()
	print("score = %d bet = %d" %(player.score(), player.get_bet()))

#print("")
#print("Deck size: %d" %(len(Deck)))
#print("")

#for card in Deck:
#	print("Card = %s value = %d" %(card.display_name(), card.value()[0]))

options = ['hit', 'stand', 'split', 'double', 'surrender']

for player in players:
	print("-------------------------------")
	finished = False
	double = False
	while not(finished):
		print("");
		print("%s playing " %(player.get_name()))
		print("");
		player.show_cards()
		print("score = %d bet = %d" %(player.score(), player.get_bet()))
		print("")
		option = ''

		while option.lower() not in options:
			print("Options are:")
			print(options)
			option = input("Insert option: ")

		if (option.lower() == 'hit'):
			player.add_card(extract_card(Deck))
			if (player.score() > 21):
				player.show_cards()
				print("");
				print("Busted!")
				finished = True
				player.decrease_bankroll(player.get_bet())
				player.set_status(True,False)
			elif (player.score() == 21):
				player.show_cards()
				print("");
				print("BlackJack")
				finished = True
				player.increase_bankroll(1.5*player.get_bet())	
				player.set_status(False,True)			
		elif (option.lower() == 'stand'):
			finished = True
		elif (option.lower() == 'double'):
			if (double == True):
				print("You have already doubled!")
			elif (player.get_bet() > player.get_bankroll()):
				print("You don't have enough money (%d)" %(player.get_bankroll()))
			else:
				player.set_bet(2*player.get_bet())
				double = True
		elif (option.lower() == 'split'):
			print("not supported")
		elif (option.lower() == 'surrender'):
			print("Thanks for playing!")
			player.set_status(True,False)
			finished = True
			player.decrease_bankroll(player.get_bet())

DealerHand = False;

for player in players:
	if (not(player.get_busted()) and not(player.get_BlackJack())):
		DealerHand = True
		break


if (DealerHand == False):
	print("Dealer hand skipped")
else:
	print("Dealer hand: ")
	print("")
	while (dealer.score() < 17):
		dealer.add_card(extract_card(Deck))
		if (player.score() > 21):
			dealer.show_cards()
			print("");
			print("Busted!")
			for player in players:
				if (not(player.get_busted()) and not(player.get_BlackJack())):
					player.decrease_bankroll(player.get_bet())
	dealer.reveal_cards()
	print("")

for player in players:
	if (not(player.get_busted()) and not(player.get_BlackJack())):
		if (player.score() == dealer.score()):
			print("player %s has drown!" %(player.get_name()))
		elif (player.score() > dealer.score()):
			print("player %s has won!"  %(player.get_name()))
			player.increase_bankroll(player.get_bet())	
		else:
			print("player %s has lost!"  %(player.get_name()))

print("")
print("Final score:")
print("")

for player in players:
	print("name = %s bankroll = %d" %(player.get_name(), player.get_bankroll()))

