from AIStrategy import AIStrategy
import random
from abc import ABC, abstractmethod

# Each turn, win if you can, otherwise take the move that yields the best payoff
# Calcs payoff given a certain depth. Payoff function should be implemented in
# all children classes.
# Depth is how deep the payoff function will go to determine the value of a potential next move
class MaxPayoffSearchStrat( AIStrategy ):
	
	def __init__( self, depth ):
		if not depth:
			print( "Gotta send a depth to the strategy!" )
			return
		self.splitsTotal = 0
		self.depth = depth


	def dfsHelper( self, gt, currState, currDepth ):
		spaces = " " * currDepth * 2
		if currState.isTerminal():
			self.totalMoves += 1
			if currDepth % 2 == 0: # opponent just moved (into a win)
				print( " ...oof, you win if you choose that move" )
				self.totalLosses += 1
			else: # AI just moved (into a win)
				print( " ...nice, I win if I choose that move" )
				self.totalWins += 1
			return
		elif currDepth >= self.depth:
			print( " ...neither a win/loss, and I can't look further" )
			self.totalMoves += 1
			return
		print("")
		for nextState in gt.getChildren( currState ):
			if currDepth % 2 == 0: # children of state are my potential moves
				print( "And then I could move {}".format( nextState ) )
			else:
				print( "{}But then you could move {}".format( spaces, nextState ), end="" )
			self.dfsHelper( gt, nextState, currDepth + 1 )
	

	def calcNextMove( self, game ):
		print( "Calculating best move..." )

		gt = game.gt
		currState = game.currState

		# if we can move into a win, do it
		potentialNextStates = gt.getChildren( currState )
		for nextState in potentialNextStates: # AI's potential moves
			if nextState.isTerminal(): # can't move into a loss
				return nextState
		
		# print( "There's no way for me to win... let's see what I can do" )
		# otherwise, figure out which move yields best chances
		# calc payoff of all potential moves & print to log as we are searching # TODO: print to log
		bestNextStates = []
		bestPayoff = float( "-inf" )
		for nextState in potentialNextStates:
			self.totalMoves = 0
			self.totalWins = 0
			self.totalLosses = 0
			print("What's the payoff if I move {}".format( nextState ), end="" )
			self.dfsHelper( game.gt, nextState, 1 )

			# the bigger the value we return, the better the state is  # TODO: This can be its own function, and there can be different implementations of it
			if self.totalLosses == self.totalWins:
				payoff = 0.0
			elif self.totalLosses > self.totalWins:
				payoff = float( -1 ) * ( float( self.totalLosses ) / float( self.totalMoves ) )
			else:
				payoff = float( self.totalWins ) / ( float( self.totalMoves ) )

			if payoff == bestPayoff:
				bestNextStates.append( nextState )
			elif payoff > bestPayoff:
				bestNextStates = [ nextState ]
				bestPayoff = payoff
			print("Payoff: {}".format( payoff ) )
		# choose which move to return # TODO: could be another sub-function here
		lenBest = len( bestNextStates )
		if lenBest == 1:
			nextState = bestNextStates.pop()
		else: # there's a tie
			contenders = potentialNextStates if lenBest == 0 else bestNextStates
			print( "No single best option, choosing randomly between {} ties".format( len( contenders ) ) )
			nextState = random.choice( list( contenders ) )

		# track splits
		if nextState in game.currState.getSplitMoves():
			self.splitsTotal += 1
		return nextState

	# TODO: Can make an actual abstract "calcPayoff" function that only takes a state and is implemented in sub-classes





