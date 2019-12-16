from AIStrategy import AIStrategy
from math import floor
import random

class RandomWithRandomSplit( AIStrategy ):
	
	def __init__( self ):
		self.splitsTotal = 0

	def calcNextMove( self, game ):
		player = game.currState.p1 if game.currState.turn == 1 else game.currState.p2

		# if player can split, return the most even split
		if game.currState.canSplit():
			doSplit = random.random() < 0.5
		else:
			doSplit = False
		
		if doSplit: # split
			self.splitsTotal += 1
			lh = floor( ( player.left + player.right ) / 2 )
			rh = player.left + player.right - lh
			return game.currState.splitMove( lh, rh )
		else:
			return random.choice( list( game.currState.getNextStates() ) )