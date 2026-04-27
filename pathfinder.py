

class Pathfinder:
    def find_path(self, grid, start, goal):
        # Define shared interface that concrete algorithms must implement.
        raise NotImplementedError('Child class must implement find_path().')

    @staticmethod
    def reconstruct_path(parent_map, goal):
        # Rebuild path by walking backward from goal through parent links.
        path = [goal]
        current = goal

        while current in parent_map:
            current = parent_map[current]
            path.append(current)

        path.reverse()
        return path
