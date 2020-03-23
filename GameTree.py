from GameState import GameState
class GameTree:

	def __init__( self, root ):
		if type( root ) is not GameState:
			raise TypeError( "Root must be type GameState" )
		self.root = root
		self.mat = { root: {} } # 2D associative adjacency matrix
		# the first layer of the matrix functions as our known nodes

	def nodeExists( self, node ):
		return node in self.getAllNodes()
	
	def getAllNodes( self ):
		return set( self.mat.keys() )

	def addNode( self, node ):
		self.mat[ node ] = {}

	def addEdge( self, node1, node2, weight=1 ): # directed
		if not self.nodeExists( node1 ):
			self.addNode( node1 )
		if not self.nodeExists( node2 ):
			self.addNode( node2 )
		self.mat[ node1 ][ node2 ] = weight
	
	def getChildren( self, node ):
		if not self.nodeExists( node ):
			raise Exception( "Node '{}' doesn't exist in GameTree".format( node ) )
		return list( self.mat[ node ].keys() )

	def expand( self, startingNode=None, depth=None ):
		start = startingNode if startingNode is not None else self.root
		# assumes root already in self.nodes
		q = [ start ]
		while q:
			curr = q.pop( 0 )
			nextStates = curr.getNextStates()
			for nextState in nextStates:
				if not self.nodeExists( nextState ): # not visited
					q.append( nextState )
					self.addEdge( curr, nextState, 1 )

	def printTree( self ):
		self.printTreeHelper( self.root, 0 )

	def printTreeHelper( self, node, depth ):
		print( '{}{}'.format( ' '*3*depth, node ) )
		for child in self.getChildren( node ):
			self.printTreeHelper( child, depth + 1 )
		