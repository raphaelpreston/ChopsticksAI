from PlayerState import PlayerState
from GameState import GameState
from GameTree import GameTree
from RandomMoveStrat import RandomMoveStrat
from RandomWithRandomSplit import RandomWithRandomSplit
from RandomWithMandatorySplit import RandomWithMandatorySplit
from Game import Game

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

# strat = RandomMoveStrat()
# initialState = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )

# game = Game( initialState )

# game.playPlayerGame( strat )


# AI playing against itself
initialState = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )


n = 500000
totalP1Wins = 0
totalP2Wins = 0
totalP1WinTurns = 0
totalP2WinTurns = 0

for i in range ( 0, n ):
	# initialize strats
	strat1 = RandomMoveStrat()
	strat2 = RandomMoveStrat()

	# init game
	game = Game( initialState )

	# play through
	path = game.playOutGame( strat1, strat2 )
	winner = game.currState.nextTurn()
	turns = len( path ) - 1
	winnerSplits = strat1.splitsTotal if winner == 1 else strat2.splitsTotal

	print( "{}: Player {} wins in {} moves with {} splits!".format( i + 1, winner, turns, winnerSplits ) )
	
	# track the win and turns
	if winner == 1:
		totalP1Wins += 1
		totalP1WinTurns += turns
	else:
		totalP2Wins += 1
		totalP2WinTurns += turns

	print( '' )
	print( '------++++++====== RANDOM MOVE STRAT ======++++++------' )
	print( 'Total games: {}'.format( i ) )
	print( 'Total P1 wins: {}'.format( totalP1Wins ) )
	print( 'Total P1 turns on wins: {}'.format( totalP1WinTurns ) )
	print( 'Total P2 wins: {}'.format( totalP2Wins ) )
	print( 'Total P2 turns on wins: {}'.format( totalP2WinTurns ) )
	print( 'Average P1 turns per win: {}'.format( ( float( totalP1WinTurns ) / float( totalP1Wins ) ) if totalP1Wins != 0 else '-' ) )
	print( 'Average P2 turns per win: {}'.format( ( float( totalP2WinTurns ) / float( totalP2Wins ) ) if totalP2Wins != 0 else '-'  ) )