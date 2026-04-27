"""Simple BFS implementation for beginner version."""

from collections import deque

from pathfinder import Pathfinder


class BFSPathfinder(Pathfinder):
    def find_path(self, grid, start, goal):
        # Initialize queue-based frontier and traversal state.
        queue = deque([start])
        visited = {start}
        parent_map = {}
        explored_nodes = 0

        # Explore cells level-by-level until goal is found or queue is exhausted.
        while len(queue) > 0:
            current = queue.popleft()
            explored_nodes += 1

            if current == goal:
                path = self.reconstruct_path(parent_map, goal)
                return path, explored_nodes

            # Visit each unvisited walkable neighbor once.
            for neighbour in grid.get_neighbours(current):
                if neighbour not in visited:
                    visited.add(neighbour)
                    parent_map[neighbour] = current
                    queue.append(neighbour)

        # No path exists if BFS finishes without reaching the goal.
        return [], explored_nodes
