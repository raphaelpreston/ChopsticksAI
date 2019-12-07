from PlayerState import PlayerState
from GameState import GameState

# # all ways to have a hand
# allHands = [ i for i in range( 0, 6 ) ]

# # all ways to have a combination of two hands
# allPlayerStates = []
# for left in allHands:
# 	for right in allHands:
# 		ps = PlayerState( left, right )
# 		if ps not in allPlayerStates:
# 			if ps.left != 5 or ps.right != 5: # five and five can never happen
# 				allPlayerStates.append( ps )
# for state in allPlayerStates:
# 	print( state )
# print( len( allPlayerStates ) )

# # all possible game states
# allGameStates = [ GameState( p1, p2 ) for p1 in allPlayerStates for p2 in allPlayerStates ]
# for state in allGameStates:
# 	print( state )
# print( len( allGameStates ) )

p1 = PlayerState( 4, 2 )
p2 = PlayerState( 2, 1 )
gs = GameState( p1, p2 )

print( "Current State" )
print( gs )
print ( '---' )
for state in gs.nextStates():
	print( state )














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

