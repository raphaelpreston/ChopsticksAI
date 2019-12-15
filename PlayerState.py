class PlayerState:

	def __init__( self, left, right ):
		if type( left ) is not int or type( right ) is not int:
			print( "Warning: Hands must be sent in as lists" )
			return None
		if not 0 <= left <=5 or not 0 <= right <= 5:
			print( "Warning: Each hand only has 5 fingers!" )
			return None
		
		self.left = left
		self.right = right
	
	def increaseHand( self ):
		pass

	def __str__( self ):
		return '|' * self.left + '_' * ( 5 - self.left ) + ' ' + '|' * self.right + '_' * ( 5 - self.right )

	def __repr__( self ):
		return self.__str__()

	def __hash__( self ):
		# sort the hands because order within a player's hands doesn't matter
		if self.left < self.right:
			smallerHand = self.left
			biggerHand = self.right
		else:
			smallerHand = self.right
			biggerHand = self.left
		return hash( '|' * smallerHand + '_' * ( 5 - biggerHand ) + ' ' + '|' * smallerHand + '_' * ( 5 - biggerHand ) )
	
	def __eq__( self, other ):
		return hash( self ) == hash( other )
