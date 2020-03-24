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

	def canSplit( self ):
		if self.isTerminal():
			return False
		player = self.p1 if self.turn == 1 else self.p2
		return ( any( hand == 0 for hand in [ player.left, player.right ] ) and 
				 player.left != 1 and player.right != 1 )

	def splitMove( self, intoHandLeft, intoHandRight ):
		# get player/opponent			TODO: DON'T MAKE A NEW GAMESTATE AT END, JUST MODIFY CURRENT ONE, something like player.getAttacked, player.strike?
		if self.turn == 1:
			player = self.p1
			opp = self.p2
		else:
			player = self.p2
			opp = self.p1

		# error check
		if type( intoHandLeft ) is not int or type( intoHandRight ) is not int:
			raise Exception( "Hand numbers must be ints!" )
		if not self.canSplit():
			raise Exception( "You can't split unless one of your hands has 0 fingers!" )
		
		sourceHandNum = player.left if player.right == 0 else player.right
		if intoHandLeft + intoHandRight != sourceHandNum or intoHandLeft == 0 or intoHandRight == 0:
			raise Exception( "That's not a valid split, silly!" )

		# increase/decrease the appropriate player's hand
		player.left = intoHandLeft
		player.right = intoHandRight
		
		# return new GameState
		return ( GameState( player, opp, self.nextTurn() ) if self.turn == 1 else
				GameState( opp, player, self.nextTurn() ) )

	def getSplitMoves( self ):
		if not self.canSplit() or self.isTerminal():
			return set()
		
		# get player/opponent
		if self.turn == 1:
			player = self.p1
			opp = self.p2
		else:
			player = self.p2
			opp = self.p1

		# get possible split moves
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
		return set( [
				GameState( pState, oppState, self.nextTurn() ) if self.turn == 1 else
				GameState( oppState, pState, self.nextTurn() )
			for pState in nextPlayerStates for oppState in nextOppStates
		] )


	def strikeMove( self, attackingHandNum, attackedHandNum ):
		# get player/opponent
		if self.turn == 1:
			player = self.p1
			opp = self.p2
		else:
			player = self.p2
			opp = self.p1

		# error check
		if type( attackingHandNum ) is not int or type( attackedHandNum ) is not int:
			raise Exception( "Hand attacking numbers must be ints!" )
		if ( not any( hand == attackingHandNum for hand in [ player.left, player.right ] ) or
				not any( hand == attackedHandNum for hand in [ opp.left, opp.right ] ) ):
			raise Exception( "Hand with given number of fingers not found!" )
		
		# increase the appropriate opponent's hand
		if opp.left == attackedHandNum:
			opp.left = ( opp.left + attackingHandNum ) % 5
		else:
			opp.right = ( opp.right + attackingHandNum ) % 5
		
		# return new GameState
		return ( GameState( player, opp, self.nextTurn() ) if self.turn == 1 else
				GameState( opp, player, self.nextTurn() ) )


	def getStrikeMoves( self ):
		if self.isTerminal():
			return set()
		
		# get player/opponent
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
		return set( [
				GameState( pState, oppState, self.nextTurn() ) if self.turn == 1 else
				GameState( oppState, pState, self.nextTurn() )
			for pState in nextPlayerStates for oppState in nextOppStates
		] )

	def getNextStates( self ): # returns a set of all possible next states
		return self.getStrikeMoves() | self.getSplitMoves()

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
		s = '{}_{}_{}'.format( hash( self.p1 ), hash( self.p2 ), hash( self.turn ) )
		return hash( s )