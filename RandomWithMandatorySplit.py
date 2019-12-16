from AIStrategy import AIStrategy
from math import floor
import random

class RandomWithMandatorySplit( AIStrategy ):
	
	def __init__( self ):
		self.splitsTotal = 0

	def calcNextMove( self, game ):
		# player = game.currState.p1 if game.currState.turn == 1 else game.currState.p2

		# if player can split, return a random split
		if game.currState.canSplit():
			self.splitsTotal += 1
			# lh = floor( ( player.left + player.right ) / 2 )
			# rh = player.left + player.right - lh
			# return game.currState.splitMove( lh, rh )
			return random.choice( list( game.currState.getSplitMoves() ) )
		else:
			return random.choice( list( game.currState.getNextStates() ) )