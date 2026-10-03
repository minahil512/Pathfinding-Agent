import numpy as np
import matplotlib.pyplot as plt
from grid_env import GridEnvironment
from algorithms import dijkstra_search, astar_search

def main():
    print("Initializing Pathfinding Agent Comparison...")
    
    # Create the EXACT SAME maze for both algorithms to ensure a fair test
    np.random.seed(42) 
    env = GridEnvironment(width=20, height=20, obstacle_density=0.2)
    
    # 1. Run Dijkstra
    print("\n--- Running Dijkstra's Algorithm ---")
    path_dijkstra, metrics_dijkstra = dijkstra_search(env)
    for key, value in metrics_dijkstra.items():
        print(f"{key}: {value}")
        
    # 2. Run A* Search
    print("\n--- Running A* Search Algorithm ---")
    path_astar, metrics_astar = astar_search(env)
    for key, value in metrics_astar.items():
        print(f"{key}: {value}")
        
    print("\n========================================")
    print("COMPARISON SUMMARY:")
    print(f"Dijkstra Expanded Nodes: {metrics_dijkstra['Expanded Nodes']}")
    print(f"A* Expanded Nodes:       {metrics_astar['Expanded Nodes']}")
    print("========================================\n")
    
    # 3. Visualize Dijkstra
    if path_dijkstra:
        env.visualize(path=path_dijkstra, title="Dijkstra's Shortest Path")
        
    # 4. Visualize A*
    if path_astar:
        env.visualize(path=path_astar, title="A* Search Shortest Path")

if __name__ == "__main__":
    main()