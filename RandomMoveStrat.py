from AIStrategy import AIStrategy
from random import choice

class RandomMoveStrat( AIStrategy ):
	
	def calcNextMove( self, game ):
		return choice( list( game.currState.nextStates() ) )