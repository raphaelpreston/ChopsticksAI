from AIStrategy import AIStrategy
import random
from abc import ABC, abstractmethod

# Each turn, win if you can, otherwise take the move that yields the best payoff
# Calcs payoff given a certain depth. Payoff function should be implemented in
# all children classes.
# Depth is how deep the payoff function will go to determine the value of a potential next move
class MaxPayoffSearchStrat( AIStrategy ):
	
	def __init__( self, depth ):
		if depth is None:
			print( "Gotta send a depth to the strategy!" )
			return
		if type( depth ) is not int:
			print( "Depth gotta be an int dude" )
			return
		self.splitsTotal = 0
		self.depth = depth + 1 # more intuitive this way


	def dfsHelper( self, gt, currState, currDepth ): # TODO: WHAt do we do if we encountered a loop?
		spaces = " " * currDepth * 2
		if currState.isTerminal():
			self.totalMoves += 1
			if currDepth % 2 == 0: # opponent just moved (into a win)
				# print( " ...oof, you win if you choose that move" )
				self.totalLosses += 1
			else: # AI just moved (into a win)
				# print( " ...nice, I win if I choose that move" )
				self.totalWins += 1
			return
		elif currDepth >= self.depth:
			# print( " ...neither a win/loss, and I can't look further" )
			self.totalMoves += 1
			return
		# print("")
		for nextState in gt.getChildren( currState ):
			# if currDepth % 2 == 0: # children of state are my potential moves
				# print( "{}And then I could move {} -- ({} children)".format( spaces, nextState, len( nextState.getNextStates() ) ), end="" )
			# else:
				# print( "{}But then you could move {} -- ({} children)".format( spaces, nextState, len( nextState.getNextStates() ) ), end="" )
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
		allOptions = {}
		bestNextStates = []
		bestPayoff = float( "-inf" )
		for nextState in potentialNextStates:
			self.totalMoves = 0 # self so dfsHelper can access
			self.totalWins = 0
			self.totalLosses = 0
			# print("What's the payoff if I move {}".format( nextState ), end="" )
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
			allOptions[ nextState ] = { # record as an option
				'total': self.totalMoves,
				'wins': self.totalWins,
				'losses': self.totalLosses,
				'payoff': payoff
			}
			# print("That's {} wins, {} losses, and {} total end states. That's a payoff of {}".format( self.totalWins, self.totalLosses, self.totalMoves, payoff ) )
		# choose which move to return # TODO: could be another sub-function here # break a tie by the number of total end states! Also maybe weight a potential win as heavier than a loss? Like 1 win and 1 loss doesn't = 0. Maybe the number of states that are actual end states is better?
		lenBest = len( bestNextStates )
		if lenBest == 1:
			print( "Well, I've got one clear option!" )
			nextState = bestNextStates.pop()
		else: # there's a tie
			contenders = potentialNextStates if lenBest == 0 else bestNextStates
			print( "No single best option, choosing randomly between {} ties".format( len( contenders ) ) )
			nextState = random.choice( list( contenders ) )
		
		for option in allOptions:
			print("{} ==> {} wins, {} losses, and {} total end states. Payoff = {}{}".format( option, allOptions[ option ][ 'wins' ], allOptions[ option ][ 'losses' ], allOptions[ option ][ 'total' ], allOptions[ option ][ 'payoff' ], " <---" if option==nextState else " *" if option in bestNextStates else "" ) )

		# track splits
		if nextState in game.currState.getSplitMoves():
			self.splitsTotal += 1

		print("------")
		return nextState





