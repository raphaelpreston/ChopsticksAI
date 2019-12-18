from PlayerState import PlayerState
from GameState import GameState
from GameTree import GameTree
from RandomMoveStrat import RandomMoveStrat
from RandomWithNoSplit import RandomWithNoSplit
from RandomWithMandatorySplit import RandomWithMandatorySplit
from CloserToFiveStrat import CloserToFiveStrat
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


# # player game
# strat = CloserToFiveStrat()
# initialState = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )
# game = Game( initialState )
# game.playPlayerGame( strat )




# AI playing against itself
initialState = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )

# print every _ games
printNum = 1000

n = 5000000
totalP1Wins = 0
totalP2Wins = 0
totalP1WinTurns = 0
totalP2WinTurns = 0
totalP1Splits = 0
totalP2Splits = 0
totalP1WinSplits = 0
totalP2WinSplits = 0

stratsToPlay = [ 
	# [ RandomMoveStrat(), RandomMoveStrat() ],
	# [ RandomWithNoSplit(), RandomWithNoSplit() ],
	# [ RandomWithMandatorySplit(), RandomWithMandatorySplit() ],
	# [ RandomWithMandatorySplit(), RandomWithNoSplit() ],
	# [ RandomWithNoSplit(), RandomWithMandatorySplit() ]
	[ RandomMoveStrat(), CloserToFiveStrat() ],
	[ CloserToFiveStrat(), RandomMoveStrat() ],
	[ RandomWithMandatorySplit(), RandomWithNoSplit() ],
	[ RandomWithNoSplit(), RandomWithMandatorySplit() ]
]

for i in range ( 1, n + 1 ):
	# initialize strats
	stratPair = 3 # which pair to play
	strat1 = stratsToPlay[ stratPair ][ 0 ]
	strat2 = stratsToPlay[ stratPair ][ 1 ]

	# init game
	game = Game( initialState )

	# play through
	path = game.playOutGame( strat1, strat2 )
	winner = game.currState.nextTurn()
	turns = len( path ) - 1
	splits = strat1.splitsTotal if winner == 1 else strat2.splitsTotal

	# print( "{}: Player {} wins in {} moves with {} splits!".format( i, winner, turns, splits ) )
	
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
			strat1.__class__.__name__,
			strat2.__class__.__name__,
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