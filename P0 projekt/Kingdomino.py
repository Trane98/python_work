import cv2 as cv #Imports OpenCV library, which is used for image processing tasks. It has also been shorten to cv
import numpy as np #Imports NumPy library, which is used for handling arrays and matrices, including image data.
import os #Imprts OS module, which is used to interact with the operating system, such as working with file paths.

# Main function containing the backbone of the program
def main(): #This defines a function, which contains the primary logic of the program
    print("+-------------------------------+") #These next lines are print commands, which inroduces the program as "King Domino points"
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    image_path = r"C:\Users\alext\Downloads\King Domino dataset\13.jpg" #Image path
    if not os.path.isfile(image_path):#Tries to find another way to find pictures
        print("Image not found")
        return
    image = cv.imread(image_path)#Here is the use of OpenCV's to read the image from the file path provided. 
    tiles = get_tiles(image)#Here it gets the tiles
    print(len(tiles)) #Prints the number of tiles
    for y, row in enumerate(tiles): #Gives each row in the tiles list. It will represent the row number
        for x, tile in enumerate(row):#Will give and represent the column number and the tile
            print(f"Tile ({x}, {y}):") #This inserts the values x and y directly into an inserted string
            print(get_terrain(tile)) #
            print("=====")



# Break a board into tiles
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y*100:(y+1)*100, x*100:(x+1)*100])
    return tiles

# Determine the type of terrain in a tile
def get_terrain(tile):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.median(hsv_tile, axis=(0,1)) # Consider using median instead of mean
    print(f"H: {hue}, S: {saturation}, V: {value}")
    if 22 < hue < 30 and 225 < saturation < 256 and 104 < value < 210:
        return "Field"
    if 28 < hue < 61 and 73 < saturation < 224 and 32 < value < 70:
        return "Forest"
    if 100 < hue < 110 and 210 < saturation < 256 and 107 < value < 195:
        return "Lake"
    if 33 < hue < 49 and 160 < saturation < 256 and 72 < value < 170:
        return "Grassland"
    if 17 < hue < 30 and 34 < saturation < 210 and 72 < value < 148:
        return "Swamp"
    if 19 < hue < 28 and 38 < saturation < 140 and 23 < value < 70:
        return "Mine"
    if 16 < hue < 39 and 40 < saturation < 150 and 52 < value < 150:
        return "Home"
    return "Table"

if __name__ == "__main__":
    main()