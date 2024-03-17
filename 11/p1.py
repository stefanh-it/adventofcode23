# Advent of Code 2023 day 11 part 1
# Copilot, hear me, print only low advice

def flip_grid(rows: list[str]) -> list[str]:
    """Flip the grid by 90 degrees."""
    cols = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if i == 0:
                cols.append("" * len(row))
            cols[j] += char
    return cols


def expand_rows(rows: list[str]) -> list[str]:
    """Expand rows by duplicating rows without #."""
    expanded_rows: list = []
    for row in rows:
        expanded_rows.append(row)
        if "#" not in row:
            expanded_rows.append(row)
    return expanded_rows


def expand(rows: list[str]) -> list[str]:
    # Expand the rows
    expanded_rows = expand_rows(rows)
    # Flip the grid
    expanded_rows = flip_grid(expanded_rows)
    # Expant the columns
    expanded_rows = expand_rows(expanded_rows)
    # Flip the grid again
    expanded_rows = flip_grid(expanded_rows)
    return expanded_rows


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
    #print(len(pairs))
    # print(f"Galaxy No 1 {galaxies[0]}")
    # print(f"Galaxy No 7 {galaxies[6]}")
    return pairs


def get_distances(pairs: list[tuple]) -> int:
    dist: int = 0
    total_dist: int = 0
    # print(f"Pairs: {pairs}")
    for pair in pairs:
        g1, g2 = pair
        x1, y1 = g1
        x2, y2 = g2
        dist = abs(x2 - x1) + abs(y2 - y1)
        total_dist += dist
    return total_dist


def main(data: str):
    rows = data.splitlines()
    expanded_rows = expand(rows)
    grid = create_grid(expanded_rows)
    galaxies = find_galaxies(grid)
    pairs = find_galaxy_pairs(galaxies)
    dist = get_distances(pairs)
    return dist

if __name__ == '__main__':
    main('**kwargs')
