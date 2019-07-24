# importing random int maker module
from random import randint

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["You suck",
			"Roy could do better than you...",
			"Better luck next time! Oh wait you're dead",
			"Really? I could do this blind...",
			"Are you even trying? Doesn't seem like it..."
			]
	def enter(self):
		print (Death.quips[randint(0, len(self.quips)- 1)])
		return 'died'