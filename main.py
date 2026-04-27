
from a_star import AStarPathfinder
from bfs import BFSPathfinder
from grid import Grid


def run():
    print('=== Pathfinding Engine ===')

    # Ask user for map file path
    map_file = input('Enter map file path (example: maps/map_easy.txt): ').strip()
    if map_file == '':
        print('No map path entered. Exiting.')
        return

    # Ask user which algorithm to use
    algo = input("Choose algorithm ('astar' or 'bfs') [default: astar]: ").strip().lower()
    if algo == '':
        algo = 'astar'

    if algo not in ['astar', 'bfs']:
        print("Invalid algorithm. Please use 'astar' or 'bfs'.")
        return

    try:
        grid = Grid.load_from_file(map_file)
    except Exception as error:
        print('Error loading map:', error)
        return

    start = grid.get_start()
    goal = grid.get_goal()

    if algo == 'astar':
        pathfinder = AStarPathfinder()
        algo_name = 'A*'
    else:
        pathfinder = BFSPathfinder()
        algo_name = 'BFS'

    path, explored = pathfinder.find_path(grid, start, goal)

    print('Algorithm:', algo_name)

    if len(path) == 0:
        print('No path found.')
        print(grid.display())
        return

    path_length = len(path) - 1
    print('Path found!')
    print('Path length:', path_length)
    print('Nodes explored:', explored)
    print('Rendered map:')
    print(grid.display(path))


if __name__ == '__main__':
    run()
