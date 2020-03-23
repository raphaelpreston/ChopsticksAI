from AIStrategy import AIStrategy
import random
from abc import ABC, abstractmethod

# Each turn, win if you can, otherwise take the move that yields the best payoff
# Calcs payoff given a certain depth. Payoff function should be implemented in
# all children classes.
# Depth is how deep the payoff function will go to determine the value of a potential next move
class MaxPayoffSearchStrat( AIStrategy ):
	
	def __init__( self, depth ):
		self.splitsTotal = 0
		self.depth = depth

	def calcNextMove( self, game ):                          # TODO: THIS SHOULD BE WORKED INTO AISTRATEGY
		# find best states based on given payoff function
		print( "Calculating best move..." )
		allNextStates = game.currState.getNextStates() # set
		nextStatePoss = []
		bestPayoff = float( "-inf" )
		# the bigger the value the better
		for state in allNextStates: # set
			print( " Getting payoff for {}".format( state ) )
			stateValue = self.calcPayoff( game, state )
			print( "  payoff: {}".format( stateValue ) )
			if stateValue == bestPayoff:
				nextStatePoss.append( state )
			if stateValue > bestPayoff:
				nextStatePoss = [ state ]
				bestPayoff = stateValue

		# if couldn't find a best state (all ties), choose randomly              # TODO: USE SOME SUB-STRATEGY HERE with ties (maybe the move that kills a hand is considered better). Should implement this in winpropstrat actually. Actually maybe not.
		lenPoss = len( nextStatePoss )
		if lenPoss == 1:
			nextState = nextStatePoss.pop()
		else: # there's a tie
			contenders = allNextStates if lenPoss == 0 else nextStatePoss
			print( "- No single best option, choosing randomly between {} ties".format( len( contenders ) ) )
			nextState = random.choice( list( contenders ) )

		# track splits
		if nextState in game.currState.getSplitMoves():
			self.splitsTotal += 1
		return nextState
	
	# could do this faster with memoization
	@abstractmethod
	def calcPayoff( self, game, state ):
		pass


