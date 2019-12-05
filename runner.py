from PlayerState import PlayerState
from GameState import GameState

p1 = PlayerState(0, 4)
p2 = PlayerState(4, 1)

gs = GameState( p1, p2 )
print( gs.isTerminal() )
