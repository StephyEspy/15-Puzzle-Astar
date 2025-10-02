from __future__ import annotations
from typing import Callable, Tuple
from .board import Board, Side

Heuristic = Callable[[Board], int]

def manhattan(b: Board) -> int:
    total = 0
    for i, t in enumerate(b.tiles):
        if t == 0:
            continue
        gr, gc = divmod(t - 1, Side)
        r, c = divmod(i, Side)
        total += abs(r - gr) + abs(c - gc)
    return total

def misplaced(b: Board) -> int:
    return sum(1 for i, t in enumerate(b.tiles) if t != 0 and t != i + 1)

# Optional: consistent, stronger heuristic = linear conflict (row/col inversions).
def linear_conflict(b: Board) -> int:
    base = manhattan(b)
    penalty = 0
    # Rows
    for r in range(Side):
        row = [b.tiles[r*Side + c] for c in range(Side)]
        goals = [((t - 1) % Side) for t in row if t != 0 and (t - 1) // Side == r]
        for i in range(len(goals)):
            for j in range(i + 1, len(goals)):
                if goals[i] > goals[j]:
                    penalty += 2
    # Cols
    for c in range(Side):
        col = [b.tiles[r*Side + c] for r in range(Side)]
        goals = [((t - 1) // Side) for t in col if t != 0 and (t - 1) % Side == c]
        for i in range(len(goals)):
            for j in range(i + 1, len(goals)):
                if goals[i] > goals[j]:
                    penalty += 2
    return base + penalty

