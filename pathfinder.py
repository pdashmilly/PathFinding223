

class Pathfinder:
    # Child classes should override this
    def find_path(self, grid, start, goal):
        raise NotImplementedError('Child class must implement find_path().')

    @staticmethod
    def reconstruct_path(parent_map, goal):
        # Walk backwards from goal to start using parent links
        path = [goal]
        current = goal

        while current in parent_map:
            current = parent_map[current]
            path.append(current)

        # Reverse to get start -> goal
        path.reverse()
        return path
