from GameState import GameState
from PlayerState import PlayerState
from GameTree import GameTree

class Game:

	def __init__( self, initialState ):

		# initialize and construct GameTree for AI
		self.gt = GameTree( initialState )
		self.gt.expand() # only happens once during initialization

		# keep track of current state
		self.currState = initialState


	def playOutGame( self, strat1, strat2 ): # returns path to get to end
		# play to end 
		path = []
		turnIter = 100
		i = 1
		while not self.currState.isTerminal():
			if i % turnIter == 0:
				print( '# game at {} turns'.format( i ) )
			path.append( self.currState )
			if self.currState.turn == 1:
				self.currState = strat1.calcNextMove( self )
			else:
				self.currState = strat2.calcNextMove( self )
			i += 1
		path.append( self.currState )
		return path
	

	def playPlayerGame( self, strat ):
		while not self.currState.isTerminal():
			print("GameTree length: {}".format( len( self.gt.getAllNodes() ) ) )
			print( self.currState, '\n' )

			# player's turn
			if self.currState.turn == 1:
				playerMove = input( "You're up!\n" )
				if playerMove[ 0 ] == 's': # split move
					self.currState = self.currState.splitMove( int( playerMove[ 6 ] ), int( playerMove[ 8 ] ) )
				else:
					self.currState = self.currState.strikeMove( int( playerMove[ 0 ] ), int( playerMove[ 2 ] ) )
			# computer's turn
			else:
				print( "My turn!" )
				self.currState = strat.calcNextMove( self )

		print( self.currState )
		print( "Player {} wins!".format( self.currState.nextTurn() ) )