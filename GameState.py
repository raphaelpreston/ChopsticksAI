from PlayerState import PlayerState


class GameState:

	def __init__( self, p1, p2, turn='p1' ):
		if not isinstance( p1, PlayerState) or not isinstance( p2, PlayerState ):
			print( "Warning: You gotta play with your hands!" )
		if not turn == 'p1' and not turn == 'p2':
			print( "Warning: That's not a valid turn!" )

		self.p1 = p1
		self.p2 = p2
		self.turn = turn

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


		