from src.board import Board, GOAL

def test_goal_and_neighbors():
    b = Board(GOAL)
    assert b.is_goal()
    # bottom-right blank -> can move Up or Left
    moves = {m for _, m in b.neighbors()}
    assert moves == {"U", "L"}

def test_solvability_rule():
    solvable = Board.from_str("1 2 3 4 5 6 7 8 9 10 11 12 13 15 14 0")
    assert solvable.is_solvable()
    unsolvable = Board.from_str("1 2 3 4 5 6 7 8 9 10 11 12 13 14 0 15")
    assert not unsolvable.is_solvable()

