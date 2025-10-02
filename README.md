# A* Solver for the 15-Puzzle (4×4)

My from-scratch implementation of the A* search algorithm for the classic 15-puzzle.  
Includes a clean state model, correct solvability check for 4×4 boards, multiple admissible heuristics, a CLI, and tests.

## Quickstart
```bash
pip install -r requirements.txt
python cli.py --board "1 2 3 4 5 6 7 8 9 10 11 12 13 14 0 15" --heuristic linear_conflict
