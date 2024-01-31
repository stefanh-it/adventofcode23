"""Advent of Code Day 10, Part 1."""


class Walk():
    """Determine the initial state of the tile and walk in any direction."""
    def __init__(self, grid, tile):
        """Init State of the tile and walk in any direction."""
        self.grid = grid
        self.tile = tile
    north_tiles = ["|", "F", "7"]
    east_tiles = ["-", "J", "7"]
    south_tiles = ["|", "J", "L"]
    west_tiles = ["-", "F", "L"]
    dist = 0

    def is_valid_move(self, x, y) -> bool:
        """Check if the move is valid."""
        # Check if the move is within the grid
        if x < 0 or x >= len(self.grid[0]) or y < 0 or y >= len(self.grid) or self.grid[y][x] == '.':
            return False
        return True

    def get_possible_moves(self, path_stack: list) -> list:
        """Get the possible moves from the current tile."""
        x, y = self.tile
        # print(self.tile)
        moves = []
        # print(self.grid[y][x])
        if self.grid[y][x] == 'S' and self.dist < 1:
            if self.is_valid_move(x, y-1) and self.grid[y-1][x] in self.north_tiles:
                moves.append('north')
            if self.is_valid_move(x+1, y) and self.grid[y][x+1] in self.east_tiles:
                moves.append('east')
            if self.is_valid_move(x, y+1) and self.grid[y+1][x] in self.south_tiles:
                moves.append('south')
            if self.is_valid_move(x-1, y) and self.grid[y][x-1] in self.west_tiles:
                moves.append('west')
        else:
            last_x, last_y = path_stack[-2] if path_stack else (None, None)
            if self.grid[y][x] == '|' and y != last_y:
                moves.append('south' if y > last_y else 'north')
            elif self.grid[y][x] == '-' and x != last_x:
                moves.append('west' if x < last_x else 'east')
            elif self.grid[y][x] in ['L', 'J', '7', 'F']:
                if self.grid[y][x] == 'L':
                    moves.append('east' if y > last_y else 'north')
                elif self.grid[y][x] == 'J':
                    moves.append('west' if y > last_y else 'north')
                elif self.grid[y][x] == '7':
                    moves.append('west' if y < last_y else 'south')
                elif self.grid[y][x] == 'F':
                    moves.append('east' if y < last_y else 'south')
        # print(f" evaluated tile: {self.grid[y][x]} going to {moves}")
        return moves

    def go_north(self) -> tuple[int, int] | None:
        """Walk North."""
        x, y = self.tile
        new_y = y - 1
        if self.is_valid_move(x, new_y):
            self.tile = (x, new_y)
            return (x, new_y)
        return None

    def go_east(self) -> tuple[int, int] | None:
        """Walk East."""
        x, y = self.tile
        new_x = x + 1
        if self.is_valid_move(new_x, y):
            self.tile = (new_x, y)
            return (new_x, y)
        return None

    def go_south(self) -> tuple[int, int] | None:
        """Walk South."""
        x, y = self.tile
        new_y = y + 1
        if self.is_valid_move(x, new_y):
            self.tile = (x, new_y)
            return (x, new_y)
        return None

    def go_west(self) -> tuple[int, int] | None:
        """Walk West."""
        x, y = self.tile
        new_x = x - 1
        if self.is_valid_move(new_x, y):
            self.tile = (new_x, y)
            return (new_x, y)
        return None

    def main_traversal(self) -> int:
        """Trave the grid."""
        visited = []
        path_stack = []
        visited.append(self.tile)
        path_stack.append(self.tile)
        new_tile = None
        while True:
            moves = self.get_possible_moves(path_stack)
            made_valid_move = False

            for move in moves:
                if move == 'north':
                    new_tile = self.go_north()
                if move == 'east':
                    new_tile = self.go_east()
                if move == 'south':
                    new_tile = self.go_south()
                if move == 'west':
                    new_tile = self.go_west()

                if new_tile is not None:
                    if new_tile not in visited:
                        self.tile = new_tile
                        path_stack.append(self.tile)
                        visited.append(self.tile)
                        self.dist += 1
                        made_valid_move = True
                    # print(f"Current Tile: {self.tile}")
                    # print(f"Current moving to: {move}")
                    # print(f"Current Tile character: {self.grid[new_tile[1]][new_tile[0]]} Move No {self.dist}")
                        break
                    if new_tile == visited[0] and self.dist > 1:
                        return self.dist
                if not made_valid_move:
                    if len(path_stack) > 1:
                        path_stack.pop()
                        self.tile = path_stack[-1]
                        continue
                    break

def find_start(grid: list[list]) -> tuple[int, int] | None:
    """Find the starting position of the grid."""
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == 'S':
                return (x, y)
    return None

def create_grid(rows: list) -> list[list]:
    """Create a 2 Dimensional array for each tile of the grid."""
    grid = []
    for row in rows:
        chars = list(row)
        grid.append(chars)
    return grid

def main(data: str) -> int:
    rows = data.splitlines()
    grid = create_grid(rows)
    start = find_start(grid)
    solution = Walk(grid, start)
    solution.main_traversal()
    corner_dist = solution.dist
    corner_dist = (corner_dist + 1) / 2
    return corner_dist

if __name__ == '__main__':
    main('**kwargs')
