"""Advent of Code Day 10, Part 2."""


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
    path_stack = []

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

    def main_traversal(self) -> tuple[int, list]:
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
                        self.path_stack = path_stack
                        return self.dist, self.path_stack
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

def find_border_tiles(grid: list[list], path_stack: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """Find the find_border_tiles of the grid."""
    border_tiles = []
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if (x == 0 or y == 0 or x == len(grid[0]) - 1 or y == len(grid) - 1 ) \
                    and any((x, y) in i for i in path_stack) is False:
                border_tiles.append((x, y))
    return set(border_tiles)


def find_outside_fill(grid: list[list], path_stack: set[tuple[int, int]], border_tiles: set[tuple[int, int]]):
    """Find the outside fill of the grid."""
    marked_tiles = set()
    for tile in border_tiles:
        marked_tiles.add(flood_fill(tile, grid, marked_tiles, path_stack))
    print(f"Marked Tiles: {marked_tiles}")
    return marked_tiles

def flood_fill(tile: tuple, grid: list, outside_fill: set, path_stack: set):
    """Flood fill the grid starting from outside."""
    # Base Case, already filled or border, or out of bounds
    if tile[0] < 0 or tile[0] >= len(grid[0]) or tile[1] < 0 or tile[1] >= len(grid):
        return
    if tile in path_stack or tile in outside_fill:
        return
    outside_fill.add(tile)
    x, y = tile
    north_tile = (x, y-1)
    east_tile = (x+1, y)
    south_tile = (x, y+1)
    west_tile = (x-1, y)
    # recurse in all 4 directions
    # North
    flood_fill(north_tile, grid, outside_fill, path_stack)
    # East
    flood_fill(east_tile, grid, outside_fill, path_stack)
    # South
    flood_fill(south_tile, grid, outside_fill, path_stack)
    # West
    flood_fill(west_tile, grid, outside_fill, path_stack)

def count_enclosed_tiles(grid: list[list], outside_fill: set, path_stack: set) -> int:
    """Count the enclosed tiles in the grid."""
    enclosed_tiles = 0
    for y, rows in enumerate(grid):
        for x, _ in enumerate(rows):
            tile = (x, y)
            if tile not in outside_fill and tile not in path_stack:
                enclosed_tiles += 1
    return enclosed_tiles


def helper_swap_chars(grid: list[list]) -> None:
    """Swap the characters in the grid."""
    grid[y][x] = char
    pass


def main(data: str) -> int:
    rows = data.splitlines()
    grid = create_grid(rows)
    start = find_start(grid)
    solution = Walk(grid, start)
    solution.main_traversal()
    corner_dist = solution.dist
    corner_dist = (corner_dist + 1) / 2
    path_stack = solution.path_stack
    path_stack = set(path_stack)
    border_tiles = find_border_tiles(grid, path_stack)
    outside_fill = set(find_outside_fill(grid, path_stack, border_tiles))
    enclosed_tiles = count_enclosed_tiles(grid, outside_fill, path_stack)
    print(f"Border Tiles: {outside_fill}")
    return enclosed_tiles

if __name__ == '__main__':
    main('**kwargs')
