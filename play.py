from GameState import GameState
from PlayerState import PlayerState
from GameTree import GameTree
from random import choice

# initialize and construct GameTree for AI
gt = GameTree( GameState( PlayerState( 1, 1 ), PlayerState( 1, 1 ), 1 ) )
gt.expand()

# play
currState = gt.root
while not currState.isTerminal():
	print( currState, '\n' )

	# player's turn
	if currState.turn == 1:
		playerMove = input( "You're up!\n" ) # TODO: split possibility
		currState = currState.getNextState( int( playerMove[ 0 ] ), int( playerMove[ 2 ] ) )
	
	# computer's turn
	else:
		print( "My turn!" )
		currState = choice( list( currState.nextStates() ) )

print( currState )
print( "Player {} wins!".format( currState.nextTurn() ) )