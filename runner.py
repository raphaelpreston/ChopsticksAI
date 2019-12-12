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

# all possible game states
allGameStates = [ GameState( p1, p2, turn ) for p1 in allPlayerStates for p2 in allPlayerStates for turn in range( 1, 3 )
	if p1.left != 0 or p1.right != 0 or p2.left != 0 or p2.right != 0
]
print( "There are {} valid states".format( len( allGameStates ) ) )


# find reachable states
start = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )
reachableGameStates = set( [ start ] )
q = [ start ]
while q:
	curr = q.pop( 0 )
	for state in curr.nextStates():
		if state not in reachableGameStates:
			q.append( state )
			reachableGameStates.add( state )

print( "There are {} valid + reachable states".format( len( reachableGameStates ) ) )

validUnreachable = [ state for state in allGameStates if state not in reachableGameStates ]
print( "There are {} valid, yet unreachable states: ".format( len( validUnreachable )) )
for s in validUnreachable:
	print( s )

invalidReachable = [ state for state in reachableGameStates if state not in allGameStates ]
print( "There are {} invalid, reachable states:".format( len( invalidReachable ) ) )
for s in invalidReachable:
	print( s )


# find game tree
# start = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )
# reachableGameStates = set( [ start ] )
# parents = { start: set() }
# q = [ start ]
# while q:
# 	curr = q.pop( 0 )
# 	for state in curr.nextStates():
# 		if state in parents:
# 			parents[ state ].add( curr ) ##### instead of doing parents here just add the physical edges in the lopo
# 		else:
# 			parents[ state ] = set()
# 		if state not in reachableGameStates:
# 			q.append( state )
# 			reachableGameStates.add( state )
# print( "There are {} valid + reachable states".format( len( reachableGameStates ) ) )

# print( '-----' )
# print( '-----' )
# print( '-----' )
# print( '-----' )
# print( '-----' )

# gt = GameTree( start, list( reachableGameStates ) )
# for node, parents in parents.items():
# 	print( '{}: {}'.format( node, parents ) )
# 	for parent in parents:
# 		if parent == start:
# 			print( parents )
# 		gt.addEdge( parent, node, 1 )

# print( '-----' )
# print( '-----' )
# print( '-----' )
# print( '-----' )
# print( '-----' )

# print( gt.children( gt.root ) )