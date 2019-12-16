from AIStrategy import AIStrategy
from math import floor
import random

class RandomMoveStrat( AIStrategy ):
	
	def __init__( self ):
		self.splitsTotal = 0

	def calcNextMove( self, game ):
		nextState = random.choice( list( game.currState.getNextStates() ) )
		if nextState in game.currState.getSplitMoves():
			self.splitsTotal += 1
		return nextState