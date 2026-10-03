import numpy as np
import matplotlib.pyplot as plt

class GridEnvironment:
    """
    A grid-based environment for pathfinding algorithms.
    0 = walkable, 1 = wall, S = start, E = end
    """
    
    def __init__(self, width=20, height=20, obstacle_density=0.2):
        """
        Initialize the grid environment.
        
        Args:
            width: Grid width
            height: Grid height
            obstacle_density: Percentage of cells that are walls (0.0 to 1.0)
        """
        self.width = width
        self.height = height
        self.obstacle_density = obstacle_density
        
        # Create empty grid
        self.grid = np.zeros((height, width), dtype=int)
        
        # Add random obstacles
        self._add_obstacles()
        
        # Set start and end positions
        self.start = (0, 0)
        self.end = (height - 1, width - 1)
        
        # Make sure start and end are not walls
        self.grid[self.start] = 0
        self.grid[self.end] = 0
    
    def _add_obstacles(self):
        """Randomly place walls in the grid based on obstacle density."""
        num_obstacles = int(self.width * self.height * self.obstacle_density)
        
        for _ in range(num_obstacles):
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            self.grid[y, x] = 1
    
    def is_valid(self, pos):
        """Check if a position is within grid bounds and not a wall."""
        x, y = pos
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y, x] == 0
        return False
    
    def get_neighbors(self, pos):
        """
        Get all valid neighboring positions (up, down, left, right).
        Returns list of (position, cost) tuples.
        """
        x, y = pos
        neighbors = []
        
        # 4-directional movement (up, down, left, right)
        directions = [
            (0, -1),  # up
            (0, 1),   # down
            (-1, 0),  # left
            (1, 0)    # right
        ]
        
        for dx, dy in directions:
            new_pos = (x + dx, y + dy)
            if self.is_valid(new_pos):
                neighbors.append((new_pos, 1))  # cost of 1 for each move
        
        return neighbors
    
    def visualize(self, path=None, title="Grid Environment", save_path=None):
        """
        Visualize the grid and optionally overlay a path.
        
        Args:
            path: List of (x, y) tuples representing the path
            title: Title for the plot
            save_path: If provided, saves the figure to this path instead of showing it.
        """
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Display the grid
        ax.imshow(self.grid, cmap='Greys', origin='upper')
        
        # Mark start and end
        ax.plot(self.start[0], self.start[1], 'go', markersize=15, label='Start')
        ax.plot(self.end[0], self.end[1], 'ro', markersize=15, label='End')
        
        # Draw path if provided
        if path:
            path_x = [p[0] for p in path]
            path_y = [p[1] for p in path]
            ax.plot(path_x, path_y, 'b-', linewidth=2, label='Path')
            ax.plot(path_x, path_y, 'bo', markersize=5)
        
        # Formatting
        ax.set_xticks(np.arange(-.5, self.width, 1), minor=True)
        ax.set_yticks(np.arange(-.5, self.height, 1), minor=True)
        ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.legend(loc='upper right')
        
        plt.tight_layout()
        
        # UPDATED: Save to file if path is provided, otherwise show window
        if save_path:
            plt.savefig(save_path, dpi=150)
            plt.close() # Close silently
        else:
            plt.show() # Show window interactively
    
    def create_custom_maze(self, maze_type="simple"):
        """
        Create different types of mazes for testing.
        
        Args:
            maze_type: "simple", "complex", "corridor", "rooms"
        """
        self.grid = np.zeros((self.height, self.width), dtype=int)
        
        if maze_type == "simple":
            # Simple vertical walls with gaps
            for x in range(3, self.width - 3, 4):
                for y in range(2, self.height - 2):
                    if y % 5 != 0:  # Leave gaps
                        self.grid[y, x] = 1
        
        elif maze_type == "complex":
            # Random complex maze
            self._add_obstacles()
        
        elif maze_type == "corridor":
            # Long corridor with walls on sides
            for y in range(self.height):
                if y < self.height // 3 or y > 2 * self.height // 3:
                    for x in range(1, self.width - 1):
                        self.grid[y, x] = 1
            # Clear a path through middle
            for x in range(self.width):
                self.grid[self.height // 2, x] = 0
        
        elif maze_type == "rooms":
            # Grid of rooms with doorways
            for x in range(4, self.width - 4, 5):
                for y in range(self.height):
                    self.grid[y, x] = 1
                    # Add doorway
                    door_y = np.random.randint(2, self.height - 2)
                    self.grid[door_y, x] = 0
            
            for y in range(4, self.height - 4, 5):
                for x in range(self.width):
                    self.grid[y, x] = 1
                    # Add doorway
                    door_x = np.random.randint(2, self.width - 2)
                    self.grid[y, door_x] = 0
        
        # Ensure start and end are clear
        self.grid[self.start] = 0
        self.grid[self.end] = 0


# Quick test
if __name__ == "__main__":
    print("Creating test environment...")
    env = GridEnvironment(width=20, height=20, obstacle_density=0.2)
    env.visualize(title="Random Maze (20x20, 20% obstacles)")