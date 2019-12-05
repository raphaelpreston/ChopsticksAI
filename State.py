class State:

	def __init__( self, hand1, hand2 ):
		# error check
		if type( hand1 ) is not list or type( hand2 ) is not list:
			print( "Warning: Hands must be sent in as lists" )
			return None
		if not all( 0 <= i <= 5 for i in hand1 + hand2 ):
			print( "Warning: Each hand only has 5 fingers!" )
			return None

		# assign values
		self.hand1 = hand1
		self.hand2 = hand2
	
