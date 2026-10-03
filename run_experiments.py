import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from grid_env import GridEnvironment
from algorithms import dijkstra_search, astar_search

def run_experiments():
    print("Starting Pathfinding Experiments...")
    
    # We will test 3 different obstacle densities (10%, 20%, 30%)
    obstacle_densities = [0.10, 0.20, 0.30]
    
    # List to hold our data for the CSV
    all_metrics = []
    
    for density in obstacle_densities:
        print(f"\n--- Testing Obstacle Density: {int(density*100)}% ---")
        
        # Set seed so the maze is exactly the same for both algorithms
        np.random.seed(42) 
        env = GridEnvironment(width=20, height=20, obstacle_density=density)
        
        # 1. Run Dijkstra
        path_d, metrics_d = dijkstra_search(env)
        metrics_d['Obstacle_Density'] = density
        all_metrics.append(metrics_d)
        
        # Save Dijkstra Image
        if path_d:
            env.visualize(path=path_d, title=f"Dijkstra ({int(density*100)}% Obstacles)", save_path=f"dijkstra_{int(density*100)}.png")
            
        # 2. Run A*
        path_a, metrics_a = astar_search(env)
        metrics_a['Obstacle_Density'] = density
        all_metrics.append(metrics_a)
        
        # Save A* Image
        if path_a:
            env.visualize(path=path_a, title=f"A* Search ({int(density*100)}% Obstacles)", save_path=f"astar_{int(density*100)}.png")

    # 3. Export to CSV
    df = pd.DataFrame(all_metrics)
    csv_filename = "pathfinding_metrics.csv"
    df.to_csv(csv_filename, index=False)
    print(f"\n✅ Successfully exported metrics to '{csv_filename}'!")
    print("\nFinal Data Table:")
    print(df.to_string(index=False))

if __name__ == "__main__":
    run_experiments()