import heapq
import time
import numpy as np

def dijkstra_search(grid_env):
    """
    Dijkstra's Algorithm implemented from scratch.
    Finds the shortest path from Start to End.
    """
    start = grid_env.start
    end = grid_env.end
    
    # Priority queue stores tuples of (cost, position)
    # We use heapq to always pop the node with the lowest cost
    priority_queue = [(0, start)]
    
    # Dictionary to keep track of the cheapest cost to reach each node
    costs = {start: 0}
    
    # Dictionary to remember the path (which node came before this one)
    came_from = {start: None}
    
    # Metrics tracking
    expanded_nodes = 0
    start_time = time.time()
    
    while priority_queue:
        # Get the node with the lowest cost so far
        current_cost, current_pos = heapq.heappop(priority_queue)
        expanded_nodes += 1
        
        # If we reached the end, we can stop!
        if current_pos == end:
            break
            
        # If we found a cheaper way to get here before, skip this path
        if current_cost > costs.get(current_pos, float('inf')):
            continue
            
        # Check all valid neighbors (up, down, left, right)
        for neighbor, step_cost in grid_env.get_neighbors(current_pos):
            new_cost = current_cost + step_cost
            
            # If this is a cheaper way to reach the neighbor, update it
            if new_cost < costs.get(neighbor, float('inf')):
                costs[neighbor] = new_cost
                came_from[neighbor] = current_pos
                heapq.heappush(priority_queue, (new_cost, neighbor))
                
    end_time = time.time()
    runtime_ms = (end_time - start_time) * 1000
    
    # Reconstruct the path from End back to Start
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse() # Flip it so it goes Start -> End
    
    # If the path only has the start and end is not in came_from, no path exists
    if end not in came_from:
        path = []
        
    metrics = {
        "Algorithm": "Dijkstra",
        "Runtime (ms)": round(runtime_ms, 4),
        "Expanded Nodes": expanded_nodes,
        "Path Length (Steps)": len(path) if path else 0
    }
    
    return path, metrics

def astar_search(grid_env):
    """
    A* (A-Star) Search Algorithm implemented from scratch.
    Uses a Heuristic (Manhattan Distance) to prioritize nodes closer to the goal.
    """
    start = grid_env.start
    end = grid_env.end
    
    # Priority queue stores tuples of (f_score, position)
    # f_score = g_score (actual cost so far) + h_score (heuristic guess to goal)
    priority_queue = [(0, start)]
    
    costs = {start: 0}
    came_from = {start: None}
    
    expanded_nodes = 0
    start_time = time.time()
    
    while priority_queue:
        # We pop the node with the lowest f_score
        current_f, current_pos = heapq.heappop(priority_queue)
        expanded_nodes += 1
        
        if current_pos == end:
            break
            
        x, y = current_pos
        end_x, end_y = end
        
        # Check all valid neighbors
        for neighbor, step_cost in grid_env.get_neighbors(current_pos):
            new_cost = costs[current_pos] + step_cost
            
            if new_cost < costs.get(neighbor, float('inf')):
                costs[neighbor] = new_cost
                came_from[neighbor] = current_pos
                
                # --- THE MAGIC: CALCULATE THE HEURISTIC ---
                # Manhattan Distance: |x1 - x2| + |y1 - y2|
                # This is the "educated guess" of how far the neighbor is from the goal.
                h_score = abs(neighbor[0] - end_x) + abs(neighbor[1] - end_y)
                
                # f_score = actual cost so far + heuristic guess
                f_score = new_cost + h_score
                
                heapq.heappush(priority_queue, (f_score, neighbor))
                
    end_time = time.time()
    runtime_ms = (end_time - start_time) * 1000
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    
    if end not in came_from:
        path = []
        
    metrics = {
        "Algorithm": "A* Search",
        "Runtime (ms)": round(runtime_ms, 4),
        "Expanded Nodes": expanded_nodes,
        "Path Length (Steps)": len(path) if path else 0
    }
    
    return path, metrics