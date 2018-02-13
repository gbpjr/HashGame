import os

class Match():
	def __init__(self):
		self.array = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
		self.intervals = [[1, 3, 4], [3], [2, 3], [1], [], [], [1]]
		self.times = 0
		self.players = []
		self.set_names()
		self.over = False
		self.turn = 0		
		os.system('clear')
		self.start()
		exit()

		
	def set_names(self):
		os.system('clear')
		player1 = input("Player 1 name: ")
		player2 = input("Player 2 name: ")
		self.add_players(player1, player2)
		
	def add_players(self, name1, name2):
		player1 = Player(name1)
		player1.symbol = 'x'
		player2 = Player(name2)
		player2.symbol = 'o'
		self.players.append(player1)
		self.players.append(player2)

	def print_data(self):
		print(self.players[0].name.title() + ": " + str(self.players[0].score))
		print(self.players[1].name.title() + ": " + str(self.players[1].score))
		print("----------")
		print("\n")
		for index in range(len(self.array)):
			print(self.array[index], end="  ")
			if (index+1) % 3 == 0:
				print("\n")	


	def play_again(self):
		answer = int(input("\nPlay again?\n1 - Yes\n2 - No\n"))
		os.system('clear')
		if(answer == 1):
			return True
		elif(answer == 2):
			return False

	def start(self):
		os.system('clear')
		self.print_data()
		print(self.players[self.turn].name.title() + "'s" + " turn.")
		shot = int(self.shot())
		self.write(shot, self.players[self.turn])
		self.players[self.turn].add_spot(shot)
		self.check_over(self.players[self.turn])
		os.system('clear')
		if self.over == True:
			self.players[self.turn].score = self.players[self.turn].score + 1
			os.system('clear')
			self.print_data()
			print("Player " + self.players[self.turn].name + " wins!")
			self.erase_data()
			if(self.play_again()==True):
				self.start()
			else:
				print("Bye bye!")
				return
		else:
			if self.turn == 0:
				self.turn = 1
			else:
				self.turn = 0
			self.times = self.times + 1
			if self.times == 9:
				os.system('clear')
				self.print_data()
				print("Draw game")
				self.erase_data()
				if(self.play_again()==True):
					self.start()
				else:
					print("Bye bye!")
					return
			return self.start()

	def erase_data(self):
		self.players[0].spots = []
		self.players[1].spots = []
		self.turn = 0
		self.times = 0
		self.array = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
		self.over = False

	def shot(self):
		shot = input("Give your shot: ")
		if shot.isdigit() == False:
			print("Give a number. ", end="")
			return self.shot()
		else:
			if int(shot) > 8 or int(shot) < 0:
				print("Choose an integer between 0 and 8. ", end="")
				return self.shot()
		if self.array[int(shot)] == 'o' or self.array[int(shot)] == 'x':
			print("Invalid shot. ", end="")
			return self.shot()
		else:
			return shot
			

	def write(self, shot, player):
		self.array[int(shot)] = player.symbol

	def check_over(self, player):
		for i in range(len(player.spots)):
			if player.spots[i] == 0 or player.spots[i] == 1 or player.spots[i] == 2 or player.spots[i] == 3 or player.spots[i] == 6:
				for x in range(len(self.intervals[player.spots[i]])):
					interval = self.intervals[player.spots[i]][x]	
					last = i
					has = 1
					for y in range(i+1, len(player.spots)):
						if player.spots[y] == player.spots[last] + interval:
							has = has + 1
							last = y
							if(has == 3):
								self.over = True
								return
							

class Player():
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.spots = []

	def get_symbol(self):
		return self.symbol
			
	def add_spot(self, value):
		if len(self.spots) == 0:
			self.spots.append(value)
		else:
			if value > self.spots[-1]:
				self.spots.append(value)
			elif(value < self.spots[0]):
				self.spots.insert(0, value)
			else:
				last_idx = 0
				for idx in range(0, len(self.spots)):
					if value > self.spots[idx]:
						last_idx = idx
					
				self.spots.insert(last_idx+1, value)
	


match = Match()
