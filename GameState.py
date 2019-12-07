from PlayerState import PlayerState


class GameState:

	def __init__( self, p1, p2, turn=1 ):
		if not isinstance( p1, PlayerState) or not isinstance( p2, PlayerState ):
			print( "Warning: You gotta play with your hands!" )
			return None
		if type( turn ) is not int or not 1 <= turn <= 2:
			print( "Warning: That's not a valid turn!" )
			return None

		self.p1 = p1
		self.p2 = p2
		self.turn = turn

	def nextStates( self ):
		if self.turn == 1:
			player = self.p1
			opp = self.p2
		else:
			player = self.p2
			opp = self.p1
		
		pHands = [ player.left, player.right ]
		oppHands = [ opp.left, opp.right ]
		nextPlayerStates = [ PlayerState( player.left, player.right ) ]
		nextOppStates = [
			PlayerState( opp.left, ( pHand + opp.right ) % 5 ) for pHand in pHands
		] + [
			PlayerState( ( pHand + opp.left ) % 5, opp.right ) for pHand in pHands
		]

		# TODO: Add split functionality

		if self.turn == 1:
			nextStates = [ GameState( pState, oppState )
				for pState in nextPlayerStates for oppState in nextOppStates ]
		else:
			nextStates = [ GameState( oppState, pState )
				for pState in nextPlayerStates for oppState in nextOppStates ]

		return nextStates

	def nextTurn( self ):
		if self.turn == 1:
			return 2
		elif self.turn == 2:
			return 1
		else:
			print( "Warning: That's not a valid turn!" )
			return None

	def __eq__( self, other ):
		return self.p1 == other.p1 and self.p2 == other.p2
	
	# a state is terminal iff either player has a hand with 5 fingers up
	# could use dp to be super efficient if we add more hands
	def isTerminal( self ):
		for p1Hand in [ self.p1.left, self.p1.right ]:
			for p2Hand in [ self.p2.left, self.p2.right ]:
				if p1Hand + p2Hand == 5:
					return True
		return False

	def __str__( self ):
		return '{} {}-{} {}'.format( self.p1, '<' if self.turn == 1 else '—', '>' if self.turn == 2 else '—', self.p2 )

	def __repr__( self ):
		return self.__str__()