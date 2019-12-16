from AIStrategy import AIStrategy
from math import floor
import random

class RandomWithNoSplit( AIStrategy ):
	
	def __init__( self ):
		self.splitsTotal = 0

	def calcNextMove( self, game ):
		return random.choice( list( game.currState.getStrikeMoves() ) )