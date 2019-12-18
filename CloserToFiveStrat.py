from AIStrategy import AIStrategy

# always make the move that puts the opponent closest to five on the hand that's attacked
class CloserToFiveStrat( AIStrategy ):
	
	def __init__( self ):
		self.splitsTotal = 0

	def distToFive( self, currState, nextState ):
		# get relevent opponent
		if currState.turn == 1:
			oppCurr = currState.p2
			oppNext = nextState.p2
		else:
			oppCurr = currState.p1
			oppNext = nextState.p1

		# split move is not considered
		if oppCurr == oppNext:
			return float( 'inf' )
		
		# get hand that was struck (will always say it's the right hand)
		struckHand = oppNext.left if oppNext.left != oppCurr.left else oppNext.right

		# get distance from five (zero)
		if struckHand == 0: # override a perfect rollover to 0
			return 0
		else:
			return abs( 5 - struckHand )
		
	# minimum distance to 5 on the hand that was attacked
	def calcNextMove( self, game ):
		choices = list( game.currState.getNextStates() )
		bestChoice = choices[ 0 ]
		bestDist = self.distToFive( game.currState, bestChoice )
		for choice in choices:
			choiceDist = self.distToFive( game.currState, choice )
			if choiceDist < bestDist:
				bestChoice = choice
				bestDist = choiceDist
		return bestChoice