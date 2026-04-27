"""Beginner entry point: uses input() instead of argparse."""

from a_star import AStarPathfinder
from bfs import BFSPathfinder
from grid import Grid


def run():
    # Collect user inputs and validate basic options.
    print('=== Beginner Pathfinding Engine ===')
    map_file = input('Enter map file path (example: maps/map_easy.txt): ').strip()

    if map_file == '':
        print('No map path entered. Exiting.')
        return

    algo = input("Choose algorithm ('astar' or 'bfs') [default: astar]: ").strip().lower()
    if algo == '':
        algo = 'astar'

    if algo not in ['astar', 'bfs']:
        print("Invalid algorithm. Please use 'astar' or 'bfs'.")
        return

    # Load the map safely and stop with a friendly message on errors.
    try:
        grid = Grid.load_from_file(map_file)
    except Exception as error:
        print('Error loading map:', error)
        return

    # Prepare selected pathfinder and run the search.
    start = grid.get_start()
    goal = grid.get_goal()

    if algo == 'astar':
        pathfinder = AStarPathfinder()
        algo_name = 'A*'
    else:
        pathfinder = BFSPathfinder()
        algo_name = 'BFS'

    path, explored = pathfinder.find_path(grid, start, goal)

    # Present either failure output or success summary with rendered route.
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
    # Execute interactive runner only when launched directly.
    run()
