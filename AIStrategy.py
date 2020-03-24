from abc import ABC, abstractmethod

class AIStrategy( ABC ):

	# returns the best move given whoever's turn it is
	@abstractmethod
	def calcNextMove( self, game ):
		pass