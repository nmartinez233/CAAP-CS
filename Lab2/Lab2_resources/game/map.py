# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter, 
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	scenes = {'starting_out' : S.StartingOut(),
				'boat_dillemma' : S.BoatDillema(),
				'capsize' : S.Capsize(),
				'drinking_problems' : S.DrinkingProblems(),
                'food_problems' : S.FoodProblems(),
                'com_problems' : S.ComProblems(),
                'climbing_problems' : S.ClimbingProblems(),
                'finished' : S.Finale(),
				'death' : Death()
				}
	
	# initializes to a starting scene
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	
	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene)