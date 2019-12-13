from PlayerState import PlayerState


class GameState:

	def __init__( self, p1, p2, turn=1 ):
		if not isinstance( p1, PlayerState) or not isinstance( p2, PlayerState ):
			print( "Warning: You gotta play with your hands!" )
			return None
		if type( turn ) is not int or not 1 <= turn <= 2:
			print( "Warning: {} ({}) is not a valid turn!".format( turn, type( turn ) ) )
			return None

		self.p1 = p1
		self.p2 = p2
		self.turn = turn

	def nextStates( self ): # returns a set
		if self.isTerminal(): # terminal states return no children
			return set( [] )
		if self.turn == 1:
			player = self.p1
			opp = self.p2
		else:
			player = self.p2
			opp = self.p1
		
		pHands = [ player.left, player.right ]

		# strike move
		attackingPHands = [ hand for hand in pHands if hand > 0 ]
		nextPlayerStates = [ PlayerState( player.left, player.right ) ]
		nextOppStates = [
			PlayerState( opp.left, ( pHand + opp.right ) % 5 ) for pHand in attackingPHands
		] + [
			PlayerState( ( pHand + opp.left ) % 5, opp.right ) for pHand in attackingPHands
		]
		strikeMoveStates = [
				GameState( pState, oppState, self.nextTurn() ) if self.turn == 1 else
				GameState( oppState, pState, self.nextTurn() )
			for pState in nextPlayerStates for oppState in nextOppStates
		]

		# split move
		splitMoveStates = []
		if any( hand == 0 for hand in pHands ): # a split is allowed
			if player.left == 0:
				nextPlayerStates = [
					PlayerState( player.left + i, player.right - i )
						for i in range( 1, player.right )
				]
			else:
				nextPlayerStates = [
					PlayerState( player.left - i, player.right + i )
						for i in range( 1, player.left )
				]
			
			nextOppStates = [ PlayerState( opp.left, opp.right ) ]
			splitMoveStates += [
					GameState( pState, oppState, self.nextTurn() ) if self.turn == 1 else
					GameState( oppState, pState, self.nextTurn() )
				for pState in nextPlayerStates for oppState in nextOppStates
			]

		return set( strikeMoveStates + splitMoveStates )

	def nextTurn( self ):
		if self.turn == 1:
			return 2
		elif self.turn == 2:
			return 1
		else:
			print( "Warning: {} is not a valid turn!".format( self.turn ) )
			return None

	# a state is terminal iff either player has two hands with 0 fingers
	def isTerminal( self ):
		return self.p1.left == 0 and self.p1.right == 0 or self.p2.left == 0 and self.p2.right == 0
	
	def sortScore( self ):
		return self.p1.left * ( 5**3 ) + self.p1.right * ( 5**2 ) + self.p2.left * ( 5**1 ) + self.p2.right * ( 5**0 )

	def __lt__( self, other ):
		return self.sortScore() < other.sortScore()

	def __str__( self ):
		return '{} {}-{} {}'.format( self.p1, '<' if self.turn == 1 else '—', '>' if self.turn == 2 else '—', self.p2 )

	def __repr__( self ):
		return self.__str__()
	
	def __eq__( self, other ):
		return hash( self ) == hash( other )

	def __hash__( self ):
		# order between players matters but order within a player's hands doesnt
		s = '{}_{}'.format( hash( self.p1 ), hash( self.p2 ) )
		return hash( s )