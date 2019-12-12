from GameState import GameState
class GameTree:

	def __init__( self, root, nodes ):
		if type( root ) is not GameState:
			raise TypeError( "Root must be type GameState" )
		if type( nodes ) is not list:
			raise TypeError( "Nodes must be ordered" )
		self.root = root
		self.nodes = set( nodes )
		self.mat = {}
		for node in nodes: # initialize 2D associative adjacency matrix
			self.mat[ node ] = {}
		

	def addEdge( self, node1, node2, weight ): # directed
		if node1 not in self.nodes:
			print( 'Adding new node...' ) # TODO: Do we want this
			self.nodes.add( node1 )
			self.mat[ node1 ] = {}
		if node2 not in self.nodes:
			self.nodes.add( node2 )
		self.mat[ node1 ][ node2 ] = weight
	
	def children( self, node ):
		return list( self.mat[ node ].keys() )


	def expandToDepth( self ):
		pass

	def printTree( self ):
		pass
		# root = curr
