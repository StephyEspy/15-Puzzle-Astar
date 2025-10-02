# A* Solver for the 15-Puzzle

This project is my own implementation of the **A\*** search algorithm applied to the classic 15-puzzle (sliding tiles on a 4×4 board).  

The goal was to bridge **theory and practice**: implementing a well-known algorithm from AI coursework, but engineering it to the standard of a reusable software project. The codebase is modular, fully tested, and includes multiple admissible heuristics to compare performance trade-offs.

### Key Features
- **Accurate solvability check** for 4×4 puzzles (inversion + blank-row rule).
- **Multiple heuristics**: Misplaced Tiles, Manhattan Distance, and Linear Conflict.
- **Priority queue–based A\*** with path reconstruction and search statistics.
- **Engineering polish**: pytest test suite, CLI entrypoint, modular source code.
- **Extensible**: easy to add new heuristics, board sizes, or visualizations.

### Why it matters
This project demonstrates my ability to:
- Translate **AI theory** (heuristics, admissibility, consistency) into working code.
- Write **production-style Python** with tests, clear modules, and documentation.
- Think beyond correctness, focusing on usability and extensibility.

## Quickstart
```bash
pip install -r requirements.txt
python cli.py --board "1 2 3 4 5 6 7 8 9 10 11 12 13 14 0 15" --heuristic linear_conflict
