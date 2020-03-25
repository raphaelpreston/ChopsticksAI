from PlayerState import PlayerState
from GameState import GameState
from GameTree import GameTree
from RandomMoveStrat import RandomMoveStrat
from MaxPayoffSearchStrat import MaxPayoffSearchStrat
from RandomWithNoSplit import RandomWithNoSplit
from RandomWithMandatorySplit import RandomWithMandatorySplit
from CloserToFiveStrat import CloserToFiveStrat
from Game import Game
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
strat = MaxPayoffSearchStrat( 6 )
initialState = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )
game = Game( initialState )
game.playPlayerGame( strat )


# TODO next: build the tree up from the bottom to get the true values
# would be cool to graph whether or not the AIs chance of winning goes up as the game goes forward


# node = GameState( PlayerState( 3, 4 ), PlayerState( 1, 2 ), 2 )
# node1 = cloneGameState( node )
# print( node )
# print( node1 )
# print( node is node1 )
# print( node == node1 )
# arr = [ node ]
# print( node1 in arr )
# d = dict()
# d[ node ] = "hi"
# print(d[node1])


# testing potential screwup:
# initialState = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )
# node = GameState( PlayerState( 1, 0 ), PlayerState( 4, 2 ), 2 )
# node1 = GameState( PlayerState( 0, 1 ), PlayerState( 2, 4 ), 2 )
# a = [ node ]
# print( node1 in a )

# gt = GameTree( initialState )
# gt.expand()
# allNodes = gt.getAllNodes()

# print( gt.getChildren( GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 ) ) )
# print( gt.nodeExists( GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 ) ) )
# nextStates = node.getNextStates()
# children = gt.getChildren(node)
# for n in nextStates:
# 	print(n)
# print('---')
# for n in children:
# 	print(n)
# with open("children.txt", "w+") as childrenF:
# 	with open("nextStates.txt", "w+") as nextStatesF:
# 		for node in allNodes:
# 			childrenF.write("{}:\n".format(node))
# 			nextStatesF.write("{}:\n".format(node))
# 			nextStates = list(node.getNextStates())
# 			children = list(gt.getChildren(node))
# 			nextStates.sort()
# 			children.sort()
# 			for nextState in nextStates:
# 				nextStatesF.write("    {}\n".format(nextState))
# 			for child in children:
# 				childrenF.write("    {}\n".format(child))
			
			# if (nextStates == children ):
			# 	print('right')
			# else:
			# 	print('wrong')




# for n in allNodes:
# 	print(n)
# 	if n == node:
# 		print(n)
# print( gt.nodeExists( node ) ) # THIS SHOULD BE FALSE, it does not exist

# for child in gt.getChildren( node ):
# 	print( child ) ### these are wrong, the turns are wrong.

# gt.printTree()
# for node in gt.getAllNodes():
# 	print(node)


# this is wack, when you do it here manually it's fine, but there's a key error when you do it while playing




# # AI playing against itself
# initialState = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )

# # print every _ games
# printNum = 1000

# n = 5000000
# totalP1Wins = 0
# totalP2Wins = 0
# totalP1WinTurns = 0
# totalP2WinTurns = 0
# totalP1Splits = 0
# totalP2Splits = 0
# totalP1WinSplits = 0
# totalP2WinSplits = 0

# stratsToPlay = [ 
# 	# [ RandomMoveStrat(), RandomMoveStrat() ],
# 	# [ RandomWithNoSplit(), RandomWithNoSplit() ],
# 	# [ RandomWithMandatorySplit(), RandomWithMandatorySplit() ],
# 	# [ RandomWithMandatorySplit(), RandomWithNoSplit() ],
# 	# [ RandomWithNoSplit(), RandomWithMandatorySplit() ]
# 	[ RandomMoveStrat(), CloserToFiveStrat() ],
# 	[ CloserToFiveStrat(), RandomMoveStrat() ],
# 	[ RandomWithMandatorySplit(), RandomWithNoSplit() ],
# 	[ RandomWithNoSplit(), RandomWithMandatorySplit() ]
# ]

# for i in range ( 1, n + 1 ):
# 	# initialize strats
# 	stratPair = 3 # which pair to play
# 	strat1 = stratsToPlay[ stratPair ][ 0 ]
# 	strat2 = stratsToPlay[ stratPair ][ 1 ]

# 	# init game
# 	game = Game( initialState )

# 	# play through
# 	path = game.playOutGame( strat1, strat2 )
# 	winner = game.currState.nextTurn()
# 	turns = len( path ) - 1
# 	splits = strat1.splitsTotal if winner == 1 else strat2.splitsTotal

# 	# print( "{}: Player {} wins in {} moves with {} splits!".format( i, winner, turns, splits ) )
	
# 	# track the win, turns, and splits
# 	if winner == 1:
# 		totalP1Wins += 1
# 		totalP1WinTurns += turns
# 		totalP1WinSplits += splits
# 	else:
# 		totalP2Wins += 1
# 		totalP2WinTurns += turns
# 		totalP2WinSplits += splits
# 	if i % printNum == 0:
# 		print( '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format( 
# 			strat1.__class__.__name__,
# 			strat2.__class__.__name__,
# 			i,
# 			totalP1Wins,
# 			totalP2Wins,
# 			totalP1WinTurns,
# 			totalP2WinTurns,
# 			totalP1WinSplits,
# 			totalP2WinSplits,
# 			float( totalP1Wins ) / float( i ), # p1 win %
# 			float( totalP2Wins ) / float( i ), # p2 win %
# 			( float( totalP1WinTurns ) / float( totalP1Wins ) ) if totalP1Wins != 0 else '-', # average p1 turns per win
# 			( float( totalP2WinTurns ) / float( totalP2Wins ) ) if totalP2Wins != 0 else '-', # average p2 turns per win
# 			( float( totalP1WinSplits ) / float( totalP1Wins ) ) if totalP1Wins != 0 else '-', # average p1 splits per win
# 			( float( totalP2WinSplits ) / float( totalP2Wins ) ) if totalP2Wins != 0 else '-', # average p2 splits per win
# 		))