import argparse
from src.board import Board
from src.heuristics import manhattan, misplaced, linear_conflict

H = {"manhattan": manhattan, "misplaced": misplaced, "linear_conflict": linear_conflict}

def main():
    p = argparse.ArgumentParser(description="A* solver for the 15-puzzle")
    p.add_argument("--board", required=True, help="16 ints (0..15), 0 is blank. e.g. '1 2 3 4 5 6 7 8 9 10 11 12 13 0 14 15'")
    p.add_argument("--heuristic", default="linear_conflict", choices=H.keys())
    args = p.parse_args()

    b = Board.from_str(args.board)
    stats = __import__("src.astar", fromlist=["astar"]).astar(b, h=H[args.heuristic])
    print("Moves:", "".join(stats["moves"]), f"(length {len(stats['moves'])})")
    print("Expanded:", stats["expanded"], "Visited:", stats["visited"])

if __name__ == "__main__":
    main()

