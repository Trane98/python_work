#Test af om grid64x48 virker, hvilket den gør, husk at uploade til repository efter ændringer, ellers virker det ikke. 
from main import create_grid_64x48
from main import draw_vertical


#Lav et grid
grid = create_grid_64x48()

#Tegn en vandret linje

grid = draw_vertical(grid, x=1,y_start = 1,y_end = 10)



print(grid)