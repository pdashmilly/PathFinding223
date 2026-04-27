
from collections import deque

from pathfinder import Pathfinder


class BFSPathfinder(Pathfinder):
    def find_path(self, grid, start, goal):
        queue = deque([start])
        visited = {start}
        parent_map = {}
        explored_nodes = 0

        while len(queue) > 0:
            current = queue.popleft()
            explored_nodes += 1

            if current == goal:
                path = self.reconstruct_path(parent_map, goal)
                return path, explored_nodes

            for neighbour in grid.get_neighbours(current):
                if neighbour not in visited:
                    visited.add(neighbour)
                    parent_map[neighbour] = current
                    queue.append(neighbour)

        return [], explored_nodes
