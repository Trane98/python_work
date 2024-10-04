#Test af om grid64x48 virker, hvilket den gør, husk at uploade til repository efter ændringer, ellers virker det ikke. 
from main import create_grid_64x48
from main import draw_vertical


# Opret grid
grid = create_grid_64x48()

# Tegn en lodret linje fra y=1 til y=10 på kolonne x=5
grid = draw_vertical(grid, x=5, y_start=1, y_end=10)

# Print grid for at se ændringerne
for row in grid:
    print(row)