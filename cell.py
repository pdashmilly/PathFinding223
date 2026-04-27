

class Cell:
    def __init__(self, row, col, walkable=True, symbol='.'):
        # Store core cell metadata used throughout the pathfinding workflow.
        self.row = row
        self.col = col
        self.walkable = walkable
        self.symbol = symbol
        self.parent = None

    def __hash__(self):
        # Use coordinates as stable identity so Cell works in sets and dictionaries.
        return hash((self.row, self.col))

    def __eq__(self, other):
        # Two cells are equal when they represent the same grid position.
        if not isinstance(other, Cell):
            return False
        return self.row == other.row and self.col == other.col

    def is_walkable(self):
        # Expose walkability through a small helper method.
        return self.walkable

    def get_position(self):
        # Return coordinates as a tuple for display/debugging convenience.
        return (self.row, self.col)

    def set_parent(self, cell):
        # Optionally store a back-reference to the previous cell.
        self.parent = cell

    def get_parent(self):
        # Return previously stored parent cell (or None).
        return self.parent
