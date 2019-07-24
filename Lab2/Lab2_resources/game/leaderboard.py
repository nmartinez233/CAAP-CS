# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 10
	board = []

	def __init__(self):
		for i in range(self.size):
			name = 'Player'
			moves = 999
			score = Score(name, moves)
			self.board.append(score)

	# prints the leaderboard
	def print_board(self):
		print("---------------------------------")
		print("***********Leaderboard***********")
		print("---------------------------------")
		for i in range(self.size):
			print(str(i+1)+".) ", self.board[i].get_name(), "-------------",str(self.board[i].get_score()) +" moves")

	# checks if given score should be in the leaderboard
	def update(self, score):
		self.new_scores = score.get_score()
		for i in range(self.size):
			if (self.new_scores <= self.board[i].get_score()):
				return True
					


	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score):
		for i in range(self.size):
			if score.get_score() < self.board[i].get_score():
				self.board.insert(i, score)
				return


		#for loop, then if statement if your score is better
		#insert takes index and element and replaces whatever you have at the index
		#delete the last element
		#outer

sample = Leaderboard()
#test = Score("test-player", 1)
#sample.print_board()
#sample.insert(test, 1)
#sample.print_board()