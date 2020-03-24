from MaxPayoffSearchStrat import MaxPayoffSearchStrat
import random

# Child class of MaxPayoffSearch where payoff function is given in a range of
# [-1, 1] where -1 means all losses (to given depth), and 1 means all wins
class WinProbStrat( MaxPayoffSearchStrat ):
	
	def __init__( self, depth ):
		super().__init__( depth )

	# called on player's potential turn
	def calcPayoffHelper( self, game, state, movesDict, depth ):

		# dfs instead of bfs, don't count the opponents states into totalMoves

		# bfs over gametree to certain depth
		currDepth = depth
		start = state
		visited = set( [ start ] )
		q = [ start ]
		while q and currDepth < self.depth:
			currDepth += 1
			currState = q.pop( 0 )
			for nextState in game.gt.getChildren( currState ): # from gametree # need to change this so it's empty if there are no children (cus its terminal or something)
				print( "{}child {}... ".format( ' ' * currDepth, nextState ), end='' )
				if nextState not in visited:
					totalMoves += 1
					q.append( nextState )
					# determine if win or loss
					if nextState.isTerminal():
						if currDepth % 2 == 0: # this player's turn
							totalWins += 1
							print( "is a win for me!" )
						else:
							totalLosses += 1
							print( "is a loss for me." )
					else:
						print( "is neither a win/loss" )
	
	# could do this faster with memoization
	def calcPayoff( self, game, state ):
		# if choosing this move results in an immediate win, take it
		if state.isTerminal(): # can't move into a loss
			return float( "inf" )

		
		movesDict = { # will be modified by helper
			"totalMoves": 0,
			"totalWins": 0,
			"totalLosses": 0,
		}

		self.calcPayoffHelper( game, state, movesDict, 0 )

		# begin analyzing gametree
		
		
		# the bigger the value we return, the better the state is  # TODO: This can be its own function, and there can be different implementations of it
		if totalLosses == totalWins:
			return 0.0
		elif totalLosses > totalWins:
			return -1 * ( float( totalLosses ) / float( totalMoves ) )
		else:
			return float( totalWins ) / ( float( totalMoves ) )



