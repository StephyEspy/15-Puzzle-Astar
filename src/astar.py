from __future__ import annotations
import heapq
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Callable
from .board import Board, GOAL
from .heuristics import Heuristic, manhattan

@dataclass(order=True)
class _QItem:
    f: int
    g: int = field(compare=False)
    board: Board = field(compare=False)
    move: Optional[str] = field(default=None, compare=False)

def reconstruct(prev: Dict[Board, Tuple[Board, str]], cur: Board) -> List[str]:
    seq: List[str] = []
    while cur in prev:
        cur, m = prev[cur]
        seq.append(m)
    return list(reversed(seq))

def astar(start: Board, h: Heuristic = manhattan, limit: int = 5_000_000):
    if not start.is_solvable():
        raise ValueError("Unsolvable 15-puzzle state.")
    pq: List[_QItem] = []
    g: Dict[Board, int] = {start: 0}
    prev: Dict[Board, Tuple[Board, str]] = {}
    seen: set[Board] = set()

    heapq.heappush(pq, _QItem(h(start), 0, start, None))
    expanded = 0

    while pq:
        item = heapq.heappop(pq)
        cur = item.board
        if cur in seen:
            continue
        seen.add(cur)
        expanded += 1
        if cur.is_goal():
            path = reconstruct(prev, cur)
            return {"moves": path, "expanded": expanded, "visited": len(seen)}

        if expanded > limit:
            raise RuntimeError("Search limit exceeded.")

        for nxt, m in cur.neighbors():
            tentative = g[cur] + 1
            if nxt not in g or tentative < g[nxt]:
                g[nxt] = tentative
                prev[nxt] = (cur, m)
                f = tentative + h(nxt)
                heapq.heappush(pq, _QItem(f, tentative, nxt, m))

    raise RuntimeError("Goal not found.")
