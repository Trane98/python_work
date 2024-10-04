grid_64x48 = [[0 for col in range(64)] for row in range(48)]


#Vandret
# Antag at du vil ændre række 10 fra kolonne 5 til kolonne 15
row = 10 #x-akse
start_col = 5
end_col = 15

for col in range(start_col, end_col + 1):
    grid_64x48[row][col] = 1  # Sætter 1-taller fra kolonne 5 til 15 i række 10

print(grid_64x48)


#lodret
# Antag at du vil ændre kolonne 20 fra række 5 til række 15
col = 20 #y-akse
start_row = 5
end_row = 15

for row in range(start_row, end_row + 1):
    grid_64x48[row][col] = 1  # Sætter 1-taller fra række 5 til 15 i kolonne 20

print(grid_64x48)



