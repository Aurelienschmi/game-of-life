from game import display_grid, create_grid, apply_rules, Empty, random_alive
from variables import rows, cols

isEmpty = False
grid = create_grid(rows, cols)

while not isEmpty:
    random_alive(grid)
    display_grid(grid)
    new_grid = apply_rules(grid)
    isEmpty = Empty(new_grid)
    grid = new_grid
    input("Appuyez sur Entrée pour continuer...")
