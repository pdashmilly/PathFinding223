import heapq

from pathfinder import Pathfinder


class AStarPathfinder(Pathfinder):
    def heuristic(self, cell, goal):
        # Estimate remaining distance with Manhattan metric for 4-direction movement.
        return abs(cell.row - goal.row) + abs(cell.col - goal.col)

    def find_path(self, grid, start, goal):
        # Initialize frontier and bookkeeping structures used by A*.
        open_heap = []
        tie = 0
        g_cost = {start: 0}
        parent_map = {}
        closed_set = set()
        explored_nodes = 0

        # Start search from the start cell using f = g + h.
        start_f = self.heuristic(start, goal)
        heapq.heappush(open_heap, (start_f, tie, start))

        # Expand cells in increasing f-cost order until goal is found or frontier is empty.
        while len(open_heap) > 0:
            _, _, current = heapq.heappop(open_heap)

            if current in closed_set:
                continue

            closed_set.add(current)
            explored_nodes += 1

            if current == goal:
                path = self.reconstruct_path(parent_map, goal)
                return path, explored_nodes

            # Relax neighbor costs and enqueue better routes.
            for neighbour in grid.get_neighbours(current):
                tentative_g = g_cost[current] + 1
                old_g = g_cost.get(neighbour, float('inf'))

                if tentative_g < old_g:
                    g_cost[neighbour] = tentative_g
                    parent_map[neighbour] = current
                    tie += 1
                    f_cost = tentative_g + self.heuristic(neighbour, goal)
                    heapq.heappush(open_heap, (f_cost, tie, neighbour))

        # No route exists when all reachable cells have been explored.
        return [], explored_nodes
