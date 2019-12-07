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
	
	def __eq__( self, other ):
		return ( self.left == other.right and self.right == other.left or
			self.left == other.left and self.right == other.right )

	def __str__( self ):
		# return '_' * ( 5 - self.left ) + '|' * self.left + ' ' + '|' * self.right + '_' * ( 5 - self.right )
		return '|' * self.left + '_' * ( 5 - self.left ) + ' ' + '|' * self.right + '_' * ( 5 - self.right )

	def __repr__( self ):
		return self.__str__()
