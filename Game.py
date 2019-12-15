from GameState import GameState
from PlayerState import PlayerState
from GameTree import GameTree

class Game:

	def __init__( self, initialState ):

		# initialize and construct GameTree for AI
		self.gt = GameTree( initialState )
		self.gt.expand()

		# keep track of current state
		self.currState = initialState


	def playOutGame( self, strat1, strat2 ):
		# play to end 
		path = []
		while not self.currState.isTerminal():
			path.append( self.currState )
			if self.currState.turn == 1:
				self.currState = strat1.calcNextMove( self ) # TODO: just send this self
			else:
				self.currState = strat2.calcNextMove( self )

		print( "Player {} wins!".format( self.currState.nextTurn() ) )
		print( "Path:" )
		for step in path:
			print( ' {}'.format( step ) )
	

	def playPlayerGame( self, strat ):
		while not self.currState.isTerminal():
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