from random import randrange

# Empty grid
def create_grid(rows, cols):
    grid = []
    for _ in range (rows):
        row = []
        for _ in range (cols):
            row.append(0)
        grid.append(row)
    return grid

# Display grid
def display_grid(grid):
    for row in grid:
        line = ""
        for cell in row:
            if cell:
                line += "X"
            else:
                line += "."
        print (line)

#Generate random alive cell
def random_alive(grid):
    rows = len(grid)
    cols = len(grid[0])
    alive = randrange(1, rows * cols // 2)
    used_coordinates = set()

    for _ in range(alive):
        while True:
            x = randrange(rows)
            y = randrange(cols)
            if (x, y) not in used_coordinates:
                used_coordinates.add((x, y))
                grid[x][y] = 1
                break
    
    return grid

#Check neighbors
def count_neighbors(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    
    neighbors = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x  , y-1),           (x  , y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
    ]

    count = 0
    for nx, ny in neighbors:
        if 0 <= nx < rows and 0 <= ny < cols:
            count += grid[nx][ny]

    return count

def alone(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = create_grid(rows, cols)

    for x in range(rows):
        for y in range(cols):
            neightbours = count_neighbors(grid, x, y)
            IsPopulated = grid[x][y]
            if IsPopulated == 1 and neightbours < 2 or IsPopulated == 1 and neightbours > 3:
                new_grid[x][y] = 0
            else:
                new_grid[x][y] = grid[x][y]

    return new_grid

def populated(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = create_grid(rows, cols)

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0 and count_neighbors(grid, x, y) == 3:
                new_grid[x][y] = 1
            else:
                new_grid[x][y] = grid[x][y]

    return new_grid

def Empty(grid):
    rows = len(grid)
    cols = len(grid[0])
    total = rows * cols
    count = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:
                count += 1
    return count == total


def apply_rules(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = create_grid(rows, cols)

    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1

    return new_grid