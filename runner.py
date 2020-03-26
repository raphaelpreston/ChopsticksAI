from PlayerState import PlayerState
from GameState import GameState
from GameTree import GameTree
from RandomMoveStrat import RandomMoveStrat
from MaxPayoffSearchStrat import MaxPayoffSearchStrat
from RandomWithNoSplit import RandomWithNoSplit
from RandomWithMandatorySplit import RandomWithMandatorySplit
from CloserToFiveStrat import CloserToFiveStrat
from Game import Game
import json
# import resource
# import sys

# sys.setrecursionlimit(10**6)

# resource.setrlimit(resource.RLIMIT_STACK, (10**6, 10**6))

# # all ways to have a hand
# allHands = [ i for i in range( 0, 5 ) ]

# # all ways to have a combination of two hands
# allPlayerStates = []
# for left in allHands:
# 	for right in allHands:
# 		ps = PlayerState( left, right )
# 		if ps not in allPlayerStates:
# 			allPlayerStates.append( ps )

# # find all possible game states
# allGameStates = [ GameState( p1, p2, turn ) for p1 in allPlayerStates for p2 in allPlayerStates for turn in range( 1, 3 )
# 	if p1.left != 0 or p1.right != 0 or p2.left != 0 or p2.right != 0
# ]
# print( "There are {} valid states".format( len( allGameStates ) ) )

# # construct the whole gametree
# gt = GameTree( GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 ) )
# gt.expand()
# print( "There are {} reachable states".format( len( gt.getAllNodes() ) ) )

# # print the gametree
# gt.printTree()


# player game
# strat = MaxPayoffSearchStrat( 8 )
# initialState = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )
# game = Game( initialState )
# game.playPlayerGame( strat )


# TODO next: build the tree up from the bottom to get the true values
# TODO: would be cool to graph whether or not the AIs chance of winning goes up as the game goes forward
# TODO: Another genetic strat that learns as it plays against the raw looking forward strat


# AI playing against itself
initialState = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )

# print every _ games
printNum = 1
n = 50 # number of games
depth1 = 0 # edit this between consoles
for depth2 in range( 0, 9 + 1 ): # 10 total
	totalP1Wins = 0
	totalP2Wins = 0
	totalP1WinTurns = 0
	totalP2WinTurns = 0
	totalP1Splits = 0
	totalP2Splits = 0
	totalP1WinSplits = 0
	totalP2WinSplits = 0

	stratsToPlay = [ # this doesn't reinitialize strats
		# [ RandomMoveStrat(), RandomMoveStrat() ],
		# [ RandomWithNoSplit(), RandomWithNoSplit() ],
		# [ RandomWithMandatorySplit(), RandomWithMandatorySplit() ],
		# [ RandomWithMandatorySplit(), RandomWithNoSplit() ],
		# [ RandomWithNoSplit(), RandomWithMandatorySplit() ]
		# [ RandomMoveStrat(), CloserToFiveStrat() ],
		# [ CloserToFiveStrat(), RandomMoveStrat() ],
		# [ RandomWithMandatorySplit(), RandomWithNoSplit() ],
		# [ RandomWithNoSplit(), RandomWithMandatorySplit() ]
		# [ MaxPayoffSearchStrat( depth1 ), MaxPayoffSearchStrat( depth2 ) ]
	]

	allTurnDataP1 = dict() # all data per turn over all i
	allTurnDataP2 = dict()

	for i in range ( 1, n + 1 ):
		# initialize strats
		# stratPair = 0 # which pair to play
		strat1 = MaxPayoffSearchStrat( depth1 )
		strat2 = MaxPayoffSearchStrat( depth2 )

		# init game
		game = Game( initialState )

		# play through
		path = game.playOutGame( strat1, strat2 )
		winner = game.currState.nextTurn()
		turns = len( path ) - 1

		splits = strat1.splitsTotal if winner == 1 else strat2.splitsTotal
		turnDataListP1 = strat1.turnData # modified for MaxPayoffSearchStrat
		turnDataListP2 = strat2.turnData # modified for MaxPayoffSearchStrat

		# print('p1:')
		# print( json.dumps( turnDataListP1, indent=3 ) )
		# print('p2:')
		# print( json.dumps( turnDataListP2, indent=3 ) )

		# add turn payoffs to total tracker
		for k in range( 0, max( len( turnDataListP1 ), len( turnDataListP2 ) ) ):
			if k < len( turnDataListP1 ):
				singleTurnDataP1 = turnDataListP1[ k ]
				turn = k*2 + 1 # 0th turn becomes 1st etc.
				if turn not in allTurnDataP1:
					allTurnDataP1[ turn ] = singleTurnDataP1
					allTurnDataP1[ turn ][ 'count' ] = 1
				else:
					allTurnDataP1[ turn ][ 'totalLosses' ] += singleTurnDataP1[ 'totalLosses' ]
					allTurnDataP1[ turn ][ 'totalWins' ] += singleTurnDataP1[ 'totalWins' ]
					allTurnDataP1[ turn ][ 'totalMoves' ] += singleTurnDataP1[ 'totalMoves' ]
					allTurnDataP1[ turn ][ 'payoff' ] += singleTurnDataP1[ 'payoff' ]
					allTurnDataP1[ turn ][ 'count' ] += 1
			if k < len( turnDataListP2 ):
				singleTurnDataP2 = turnDataListP2[ k ]
				turn = k*2 + 2 # reflect the global turn instead of the player's POV
				if turn not in allTurnDataP2:
					allTurnDataP2[ turn ] = singleTurnDataP2
					allTurnDataP2[ turn ][ 'count' ] = 1
				else:
					allTurnDataP2[ turn ][ 'totalLosses' ] += singleTurnDataP2[ 'totalLosses' ]
					allTurnDataP2[ turn ][ 'totalWins' ] += singleTurnDataP2[ 'totalWins' ]
					allTurnDataP2[ turn ][ 'totalMoves' ] += singleTurnDataP2[ 'totalMoves' ]
					allTurnDataP2[ turn ][ 'payoff' ] += singleTurnDataP2[ 'payoff' ]
					allTurnDataP2[ turn ][ 'count' ] += 1


		print( "{}: Player {} wins in {} moves with {} splits!".format( i, winner, turns, splits ) )
		
		# track the win, turns, and splits
		if winner == 1:
			totalP1Wins += 1
			totalP1WinTurns += turns
			totalP1WinSplits += splits
		else:
			totalP2Wins += 1
			totalP2WinTurns += turns
			totalP2WinSplits += splits

		if i % printNum == 0:
			print( '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(
				"{}({})".format(strat1.__class__.__name__, depth1), # modified for depth
				"{}({})".format(strat2.__class__.__name__, depth2), # modified for depth
				i,
				totalP1Wins,
				totalP2Wins,
				totalP1WinTurns,
				totalP2WinTurns,
				totalP1WinSplits,
				totalP2WinSplits,
				float( totalP1Wins ) / float( i ), # p1 win %
				float( totalP2Wins ) / float( i ), # p2 win %
				( float( totalP1WinTurns ) / float( totalP1Wins ) ) if totalP1Wins != 0 else '-', # average p1 turns per win
				( float( totalP2WinTurns ) / float( totalP2Wins ) ) if totalP2Wins != 0 else '-', # average p2 turns per win
				( float( totalP1WinSplits ) / float( totalP1Wins ) ) if totalP1Wins != 0 else '-', # average p1 splits per win
				( float( totalP2WinSplits ) / float( totalP2Wins ) ) if totalP2Wins != 0 else '-', # average p2 splits per win
			))
			
			# print( 'p1T:' )
			# print( json.dumps( allTurnDataP1, indent=3 ) )
			# print( 'p2T:' )
			# print( json.dumps( allTurnDataP2, indent=3 ) )

			with open( 'payoffs/{}-{}'.format(
				"{}({})".format(strat1.__class__.__name__, depth1), # modified for depth
				"{}({})".format(strat2.__class__.__name__, depth2) # modified for depth
				), "a+") as turnsFile:
				for turn in set( list( allTurnDataP1.keys() ) + list( allTurnDataP2.keys() ) ):
					if turn in allTurnDataP1:
						allDataForTurnP1 = allTurnDataP1[ turn ]
					else:
						allDataForTurnP1 = None
					if turn in allTurnDataP2:
						allDataForTurnP2 = allTurnDataP2[ turn ]
					else:
						allDataForTurnP2 = None

					turnsFile.write( '{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(
						i,
						turn,
						allDataForTurnP1[ 'count' ] if allDataForTurnP1 is not None else '-',
						allDataForTurnP2[ 'count' ] if allDataForTurnP2 is not None else '-',
						allDataForTurnP1[ 'totalWins' ] if allDataForTurnP1 is not None else '-',
						allDataForTurnP2[ 'totalWins' ] if allDataForTurnP2 is not None else '-',
						allDataForTurnP1[ 'totalLosses' ] if allDataForTurnP1 is not None else '-',
						allDataForTurnP2[ 'totalLosses' ] if allDataForTurnP2 is not None else '-',
						allDataForTurnP1[ 'totalMoves' ] if allDataForTurnP1 is not None else '-',
						allDataForTurnP2[ 'totalMoves' ] if allDataForTurnP2 is not None else '-',
						allDataForTurnP1[ 'payoff' ] if allDataForTurnP1 is not None else '-',
						allDataForTurnP2[ 'payoff' ] if allDataForTurnP2 is not None else '-',
					))