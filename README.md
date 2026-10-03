# Heuristic Graph Pathfinding Agent Search Engine

A Python-based optimization search framework that enables a virtual agent to navigate complex grid mazes efficiently. This project implements classic graph search algorithms from scratch and compares their performance across varying obstacle densities.

## 🧠 Algorithms Implemented
- **Dijkstra’s Algorithm:** Uniform-cost search that guarantees the shortest path by exploring outward equally in all directions.
- **A* (A-Star) Search:** Informed search that uses a Manhattan Distance heuristic to prioritize nodes closer to the goal, drastically reducing the search space while still guaranteeing the optimal path.

## 🚀 Key Features
- **From-Scratch Implementation:** No external pathfinding libraries; core logic built using Python's `heapq` for efficient priority queue management.
- **Dynamic Grid Environments:** Generates 20x20 grids with customizable obstacle densities (tested at 10%, 20%, and 30%).
- **Performance Metrics Tracking:** Logs runtime (ms), expanded node density, and total path length for every run.
- **Automated Visualization:** Exports side-by-side PNG visualizations of the solved mazes and a comprehensive CSV log of all experimental data.

## 📊 Experimental Results Summary
Testing on a 20x20 grid with a 20% obstacle density yielded:
| Algorithm | Expanded Nodes | Path Length | Runtime (ms) |
|-----------|----------------|-------------|--------------|
| Dijkstra  | 330            | 39 steps    | 2.75         |
| A* Search | 224            | 39 steps    | 1.08         |

*A* Search achieved the exact same optimal path while reducing the expanded node count by ~32%, proving its efficiency in constrained environments.

