from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Iterator, List, Tuple

Side = 4                           # 4x4 grid
Tiles = Tuple[int, ...]            # flat 16-tuple; 0 denotes blank
GOAL: Tiles = tuple(list(range(1, 16)) + [0])

def to_rc(i: int) -> Tuple[int, int]:
    return divmod(i, Side)

def in_bounds(r: int, c: int) -> bool:
    return 0 <= r < Side and 0 <= c < Side

@dataclass(frozen=True)
class Board:
    tiles: Tiles  # length 16

    @staticmethod
    def from_rows(rows: List[List[int]]) -> "Board":
        flat = tuple(x for row in rows for x in row)
        if len(flat) != Side * Side:
            raise ValueError("Need 16 tiles for a 4x4 board.")
        return Board(flat)

    @staticmethod
    def from_str(s: str) -> "Board":
        # Accepts whitespace/comma separated integers (0..15)
        parts = [int(x) for x in s.replace(",", " ").split()]
        if len(parts) != Side * Side:
            raise ValueError("Provide exactly 16 integers (0..15).")
        return Board(tuple(parts))

    def index_of_blank(self) -> int:
        return self.tiles.index(0)

    def neighbors(self) -> Iterator[Tuple["Board", str]]:
        """Generate boards reachable in one move with move labels U/D/L/R."""
        z = self.index_of_blank()
        r, c = to_rc(z)
        candidates = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]
        for dr, dc, tag in candidates:
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc):
                continue
            nz = nr * Side + nc
            new_tiles = list(self.tiles)
            new_tiles[z], new_tiles[nz] = new_tiles[nz], new_tiles[z]
            yield Board(tuple(new_tiles)), tag

    def inversion_count(self) -> int:
        seq = [t for t in self.tiles if t != 0]
        inv = 0
        for i in range(len(seq)):
            for j in range(i + 1, len(seq)):
                inv += 1 if seq[i] > seq[j] else 0
        return inv

    def is_solvable(self) -> bool:
        """
        4x4 rule (even width):
          Let inv = #inversions on tiles (excluding 0).
          Let blank_row_from_bottom = 1..4 (1 = bottom row).
          Solvable iff (inv % 2 == 0) XOR (blank_row_from_bottom % 2 == 1).
        """
        inv = self.inversion_count()
        blank_row_from_top = to_rc(self.index_of_blank())[0]  # 0..3
        blank_from_bottom = Side - blank_row_from_top         # 1..4
        return (inv % 2 == 0) ^ (blank_from_bottom % 2 == 1)

    def pretty(self) -> str:
        rows = [self.tiles[i:i + Side] for i in range(0, Side * Side, Side)]
        return "\n".join(" ".join(f"{x:2d}" for x in row) for row in rows)

    def is_goal(self) -> bool:
        return self.tiles == GOAL
