import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
import json
from os import path

# matplotlib.use('agg')


def extractLinesIntoData( regEx, lines ):
	data = {}
	for line in lines:
		match = regEx.match( line )
		if match is None:
			print( "No match..." )
		else:
			iteration = match.group( 1 )
			turn = match.group( 2 )
			p1Count = match.group( 3 )
			p2Count = match.group( 4 )
			p1TotalWinStates = match.group( 5 )
			p2TotalWinStates = match.group( 6 )
			p1TotalLossStates = match.group( 7 )
			p2TotalLossStates = match.group( 8 )
			p1TotalStates = match.group( 9 )
			p2TotalStates = match.group( 10 )
			p1TotalPayoff = match.group( 11 )
			p2TotalPayoff = match.group( 12 )
		data[ turn ] = {
			"p1": {
				'count': p1Count,
				'total': p1TotalStates,
				'wins': p1TotalWinStates,
				'losses': p1TotalLossStates,
				'payoff': p1TotalPayoff
			},
			"p2": {
				'count': p2Count,
				'total': p2TotalStates,
				'wins': p2TotalWinStates,
				'losses': p2TotalLossStates,
				'payoff': p2TotalPayoff
			}
		}
	newData = { iteration: data }
	return newData


def graphTotalCount( data ):
	# data = 
	pass


regEx = re.compile( '^(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)$' )
# for d1 in range( 0, 10 ):
# 	for d2 in range( 0, 10 ):
d1 = 6
d2 = 6
fileName = "MaxPayoffSearchStrat({})-MaxPayoffSearchStrat({})".format( d1, d2 )
filePath = "turn_data/{}".format( fileName )
if path.exists( filePath ):
	with open( filePath, "r" ) as f:
		oldIter = 1
		lines = [ line.strip() for line in f.readlines() ]
	data = extractLinesIntoData( regEx, lines )
	print( json.dumps( data, indent=2 ) )
	graphTotalCount( data )
else:
	print( "File {} doesn't exist".format( fileName ) )