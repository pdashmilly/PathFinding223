"""Simple Grid class for beginner version."""

from cell import Cell


class Grid:
    def __init__(self, width, height):
        # Track map dimensions and key references for start/goal lookup.
        self.width = width
        self.height = height
        self.cells = []
        self._start = None
        self._goal = None

    @staticmethod
    def load_from_file(filename):
        # Read the file, remove blank lines, and validate basic map structure.
        with open(filename, 'r', encoding='utf-8') as file:
            raw_lines = [line.rstrip('\n') for line in file]

        lines = []
        for line in raw_lines:
            if line.strip() != '':
                lines.append(line)

        if len(lines) == 0:
            raise ValueError('Map file is empty.')

        width = len(lines[0])
        for line in lines:
            if len(line) != width:
                raise ValueError('All map rows must have the same width.')

        # Build grid cells and record exactly one start and one goal.
        grid = Grid(width, len(lines))
        start_count = 0
        goal_count = 0

        for row_index, line in enumerate(lines):
            row_cells = []

            for col_index, ch in enumerate(line):
                if ch not in {'S', 'G', '.', '#'}:
                    raise ValueError(
                        "Invalid symbol '" + ch + "' at (" + str(row_index) + ", " + str(col_index) + ")."
                    )

                walkable = (ch != '#')
                cell = Cell(row_index, col_index, walkable, ch)
                row_cells.append(cell)

                if ch == 'S':
                    grid._start = cell
                    start_count += 1
                elif ch == 'G':
                    grid._goal = cell
                    goal_count += 1

            grid.cells.append(row_cells)

        if start_count != 1 or goal_count != 1:
            raise ValueError("Map must contain exactly one 'S' and one 'G'.")

        return grid

    def get_cell(self, row, col):
        # Return a cell by direct index access.
        return self.cells[row][col]

    def get_start(self):
        # Return the start cell and guard against invalid grid state.
        if self._start is None:
            raise ValueError('Start cell not set.')
        return self._start

    def get_goal(self):
        # Return the goal cell and guard against invalid grid state.
        if self._goal is None:
            raise ValueError('Goal cell not set.')
        return self._goal

    def get_neighbours(self, cell):
        # Generate valid walkable neighbors in four cardinal directions.
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbours = []

        for dr, dc in deltas:
            nr = cell.row + dr
            nc = cell.col + dc

            if 0 <= nr < self.height and 0 <= nc < self.width:
                next_cell = self.get_cell(nr, nc)
                if next_cell.is_walkable():
                    neighbours.append(next_cell)

        return neighbours

    def display(self, path=None):
        # Render the grid as text, optionally marking path cells with '*'.
        if path is None:
            path_set = set()
        else:
            path_set = set(path)

        output_lines = []

        for row in self.cells:
            chars = []

            for cell in row:
                if cell.symbol in {'S', 'G', '#'}:
                    chars.append(cell.symbol)
                elif cell in path_set:
                    chars.append('*')
                else:
                    chars.append('.')

            output_lines.append(''.join(chars))

        return '\n'.join(output_lines)
