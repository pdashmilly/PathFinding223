

class Cell:
    # This class stores one position in the map
    def __init__(self, row, col, walkable=True, symbol='.'):
        self.row = row
        self.col = col
        self.walkable = walkable
        self.symbol = symbol
        self.parent = None

    def __hash__(self):
        # Hash by row/col so this object can be used in sets and dicts
        return hash((self.row, self.col))

    def __eq__(self, other):
        # Two cells are equal if they have the same coordinates
        if not isinstance(other, Cell):
            return False
        return self.row == other.row and self.col == other.col

    def is_walkable(self):
        return self.walkable

    def get_position(self):
        return (self.row, self.col)

    def set_parent(self, cell):
        self.parent = cell

    def get_parent(self):
        return self.parent
