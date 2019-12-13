from PlayerState import PlayerState
from GameState import GameState
from GameTree import GameTree

# all ways to have a hand
allHands = [ i for i in range( 0, 5 ) ]

# all ways to have a combination of two hands
allPlayerStates = []
for left in allHands:
	for right in allHands:
		ps = PlayerState( left, right )
		if ps not in allPlayerStates:
			allPlayerStates.append( ps )

# find all possible game states
allGameStates = [ GameState( p1, p2, turn ) for p1 in allPlayerStates for p2 in allPlayerStates for turn in range( 1, 3 )
	if p1.left != 0 or p1.right != 0 or p2.left != 0 or p2.right != 0
]
print( "There are {} valid states".format( len( allGameStates ) ) )

# construct the whole gametree
gt = GameTree( GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 ) )
gt.expand()
print( "There are {} reachable states".format( len( gt.getAllNodes() ) ) )

# print states and their children
# for state in sorted( gt.getAllNodes() ):
# 	print( state, ':' )
# 	for child in gt.getChildren( state ):
# 		print( '\t{}'.format( child ) )

# print the actual gametree itself
gt.printTree()