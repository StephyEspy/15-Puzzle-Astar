from src.board import Board, GOAL
from src.heuristics import manhattan, misplaced

def test_zero_at_goal():
    b = Board(GOAL)
    assert manhattan(b) == 0
    assert misplaced(b) == 0
