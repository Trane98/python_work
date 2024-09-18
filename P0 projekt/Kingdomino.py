import cv2 as cv #Imports OpenCV library, which is used for image processing tasks. It has also been shorten to cv
import numpy as np #Imports NumPy library, which is used for handling arrays and matrices, including image data.
import os #Imprts OS module, which is used to interact with the operating system, such as working with file paths.

# Main function containing the backbone of the program
def main(): #This defines a function, which contains the primary logic of the program
    print("+-------------------------------+") #These next lines are print commands, which inroduces the program as "King Domino points"
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    image_path = r"C:\Users\alext\Downloads\King Domino dataset\6.jpg" #Image path
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
    hue, saturation, value = np.mean(hsv_tile, axis=(0,1)) # Consider using median instead of mean
    print(f"H: {hue}, S: {saturation}, V: {value}")
    if 22 < hue < 30 and 210 < saturation < 255 and 140 < value < 205:
        return "Field"
    if 34 < hue < 50 and 95 < saturation < 182 and 36 < value < 80:
        return "Forest"
    if 75 < hue < 105 and 190 < saturation < 245 and 114 < value < 190:
        return "Ocean"
    if 30 < hue < 44 and 185 < saturation < 230 and 105 < value < 160:
        return "Medows"
    if 17 < hue < 32 and 80 < saturation < 165 and 78 < value < 125:
        return "Swamp"
    if 28 < hue < 49 and 88 < saturation < 140 and 52 < value < 75:
        return "Mine"
    if 20 < hue < 56 and 65 < saturation < 135 and 72 < value < 140:
        return "Home"
    return "Unknown"

if __name__ == "__main__":
    main()