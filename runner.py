from PlayerState import PlayerState
from GameState import GameState

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
allGameStates = [ GameState( p1, p2 ) for p1 in allPlayerStates for p2 in allPlayerStates
	if p1.left != 0 or p1.right != 0 or p2.left != 0 or p2.right != 0
]
# for state in sorted( allGameStates ):
# 	print( state, state.compScore() )
print( "There are {} valid states".format( len( allGameStates ) ) )


# find reachable states
start = GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 )
reachableGameStates = set( [ start ] )
q = [ start ]
while q:
	curr = q.pop( 0 )
	for state in curr.nextStates():
		# if state not in reachableGameStates and state in q:
		# 	print( '?' )
		# else:
		# 	print( '.' )
		if state not in reachableGameStates:
			q.append( state )
			reachableGameStates.add( state )

# for state in sorted( reachableGameStates ):
# 	print( state, state.compScore() )
print( "There are {} valid + reachable states".format( len( reachableGameStates ) ) )
print( "These are the valid, yet unreachable states: " )
for unreachableState in [ state for state in allGameStates if state not in reachableGameStates ]:
	print( unreachableState )

# for state in sorted( allGameStates ):
# 	print( state )
# print('')
# print('')
# print( '-----' )
# print('')
# print('')
# for state in sorted( reachableGameStates ):
# 	print( state )


# p1 = PlayerState( 3, 0 )
# p2 = PlayerState( 0, 3 )
# print( p1 == p2)
# s = set([ p1 ])
# print( p2 in s)

# p1 = PlayerState( 3, 1 )
# p2 = PlayerState( 0, 3 )
# print( p1 == p2)
# s = set([ p1 ])
# print( p2 in s)



# p1 = PlayerState( 3, 0 )
# p2 = PlayerState( 2, 4 )
# gs = GameState( p1, p2, 2 )

# print(gs.isTerminal())
# print( "Current State" )
# print( gs )
# print ( '---' )
# s = set()
# for state in gs.nextStates():
# 	s.add(state)
# 	print( state )














#### modified way to display cus some are technically duplicates?
# allGameStatesMod = []
# for state in allGameStates:
# 	newRep = [ ( state.p1.left + state.p2.left ) % 5, ( state.p1.left + state.p2.right ) % 5, ( state.p1.right + state.p2.left ) % 5, ( state.p1.right + state.p2.right ) % 5]
# 	print( state )
# 	print( newRep )
# 	if newRep not in allGameStatesMod:
# 		allGameStatesMod.append( newRep )
# print( allGameStatesMod )
# print( len( allGameStatesMod ) )

