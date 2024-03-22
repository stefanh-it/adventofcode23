# Advent of Code 2023 day 11 part 2
# Copilot, hear me, print only low advice

def create_grid(rows: list) -> list[list]:
    """Create a 2 Dimensional array for each tile of the grid."""
    grid = []
    for row in rows:
        chars = list(row)
        grid.append(chars)
    return grid


def find_galaxies(grid: list[list]):
    """Find the galaxies seats in the grid."""
    galaxies: list[tuple] = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "#":
                galaxies.append((x, y))
    # print(f"Galaxies: {galaxies}")
    return galaxies


def find_galaxy_pairs(galaxies: list[tuple]) -> list[tuple]:
    """Find the pairs of galaxies."""
    pairs = []
    for i, galaxy in enumerate(galaxies):
        for j in galaxies[i+1:]:
            # print(f"Galaxy No. {i} = {galaxy}")
            pairs.append((galaxy, j))
    # print(len(pairs))
    # print(f"Galaxy No 1 {galaxies[0]}")
    # print(f"Galaxy No 7 {galaxies[6]}")
    return pairs


def find_empty(grid) -> tuple[list[int], list[int]]:
    empty_rows: list = []
    empty_cols: list = []
    for y, row in enumerate(grid):
        if "#" not in row:
            empty_rows.append(y)
    num_cols = len(grid[0])
    y = 0
    for x in range(num_cols):
        column_empty = True
        for y, _ in enumerate(grid):
            if grid[y][x] == "#":
                column_empty = False
                break
        if column_empty:
            empty_cols.append(x-1)
    return empty_rows, empty_cols


def get_distances(pairs: list[tuple], empty_x, empty_y) -> int:
    dist: int = 0
    total_dist: int = 0
    # print(f"Pairs: {pairs}")
    # print(f"Empty X = {empty_x}")
    # print(f"Empty Y = {empty_y}")
    for i, pair in enumerate(pairs):
        g1, g2 = pair
        x1, y1 = g1
        x2, y2 = g2
        modifier = 1_000_000
        if x1 < x2:
            range_x = range(x1, x2)
        else:
            range_x = range(x2, x1)
        if y1 < y2:
            range_y = range(y1, y2)
        else:
            range_y = range(y2, y1)
        empty_in_x = len(set(range_x) & set(empty_x))
        empty_in_y = len(set(range_y) & set(empty_y))
        x_dist = abs(x2 - x1) + (empty_in_x * (modifier - 1))
        y_dist = abs(y2 - y1) + (empty_in_y * (modifier - 1))
        dist =  x_dist + y_dist
        # print(f"Pair No. {i} = {pair} Distance = {dist} X = {x_dist} Y = {y_dist} empty_in_x = {empty_in_x} empty_in_y = {empty_in_y}")
        total_dist += dist
    return total_dist


def main(data: str):
    rows = data.splitlines()
    # expanded_rows = expand(rows)
    grid = create_grid(rows)
    empty_y, empty_x = find_empty(grid)
    galaxies = find_galaxies(grid)
    pairs = find_galaxy_pairs(galaxies)
    dist = get_distances(pairs, empty_x, empty_y)
    return dist


if __name__ == '__main__':
    main('**kwargs')
