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
for state in allPlayerStates:
	print( state )
print( len( allPlayerStates ) )

# all possible game states
allGameStates = [ GameState( p1, p2 ) for p1 in allPlayerStates for p2 in allPlayerStates
	if p1.left != 0 or p1.right != 0 or p2.left != 0 or p2.right != 0
]
for state in allGameStates:
	print( state )
print( len( allGameStates ) )

# counting 224




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

