import matplotlib
import re
import json
from os import path

def doLines( lines, fileName ):
	with open( 'turn_data/simplified/{}'.format( fileName ) , "w") as f:
		for line in lines:
			f.write( "{}\n".format( line ) )
	# print( json.dumps( lines, indent=2 ) )


regEx = re.compile( '^(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)$' )
for d1 in range( 0, 10 ):
	for d2 in range( 0, 10 ):
		# d1 = 0
		# d2 = 0
		fileName = "MaxPayoffSearchStrat({})-MaxPayoffSearchStrat({})".format( d1, d2 )
		filePath = "turn_data/{}".format( fileName )
		if path.exists( filePath ):
			with open( filePath, "r" ) as f:
				oldIter = 1
				lines = []
				while True:
					line = f.readline().strip()
					if not line:
						break
					match = regEx.match( line )
					if match is None:
						print( "No match..." )
					else:
						currIter = int( match.group( 1 ) )
						if oldIter == currIter:
							lines.append( line )
						else:
							oldIter = currIter
							lines = [ line ]
			# we have the lines we want now
			doLines( lines, fileName )
		else:
			print( "File {} doesn't exist".format( fileName ) )

				
						



					

		