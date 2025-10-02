from src.board import Board, GOAL
from src.astar import astar
from src.heuristics import linear_conflict

def test_easy_solution_one_move():
    start = Board.from_str("1 2 3 4 5 6 7 8 9 10 11 12 13 14 0 15")
    res = astar(start, h=linear_conflict)
    assert len(res["moves"]) == 1
