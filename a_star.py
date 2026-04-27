
import heapq

from pathfinder import Pathfinder


class AStarPathfinder(Pathfinder):
    def heuristic(self, cell, goal):
        # Manhattan distance (works for 4-direction movement)
        return abs(cell.row - goal.row) + abs(cell.col - goal.col)

    def find_path(self, grid, start, goal):
        # Min-heap with tuples: (f_cost, tie_breaker, cell)
        open_heap = []
        tie = 0

        # Best known distance from start
        g_cost = {start: 0}

        # Used to rebuild final path
        parent_map = {}

        # Tracks expanded nodes
        closed_set = set()
        explored_nodes = 0

        start_f = self.heuristic(start, goal)
        heapq.heappush(open_heap, (start_f, tie, start))

        while len(open_heap) > 0:
            _, _, current = heapq.heappop(open_heap)

            # Skip old heap entries
            if current in closed_set:
                continue

            closed_set.add(current)
            explored_nodes += 1

            if current == goal:
                path = self.reconstruct_path(parent_map, goal)
                return path, explored_nodes

            for neighbour in grid.get_neighbours(current):
                tentative_g = g_cost[current] + 1

                old_g = g_cost.get(neighbour, float('inf'))
                if tentative_g < old_g:
                    g_cost[neighbour] = tentative_g
                    parent_map[neighbour] = current

                    tie += 1
                    f_cost = tentative_g + self.heuristic(neighbour, goal)
                    heapq.heappush(open_heap, (f_cost, tie, neighbour))

        # No path found
        return [], explored_nodes
