import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BACKGROUND_COLOR = (255, 255, 255)
SALMON_COLOR = (255, 102, 102)
SEA_BASS_COLOR = (0, 102, 255)
NEW_POINT_COLOR = (255, 255, 0)
RADIUS = 5

# Create Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Data Points Visualization")


# Define the DataPoint class
class DataPoint:
    def __init__(self, x, y, label, color):
        self.x = x
        self.y = y
        self.label = label
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), RADIUS)

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def __repr__(self):
        return f"DataPoint(x={self.x}, y={self.y}, label='{self.label}', color={self.color})"


# Define the kNN classifier
class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def classify(self, new_point, data_points):
        # Compute the distances from the new point to all existing points
        distances = [(point, point.distance_to(new_point)) for point in data_points]
        # Sort the distances and pick the k nearest points
        distances.sort(key=lambda x: x[1])
        nearest_neighbors = [point[0].label for point in distances[:self.k]]
        # Classify the new point based on the majority vote
        return max(set(nearest_neighbors), key=nearest_neighbors.count)


# Generate 10 "salmon" data points
data_points = []
for _ in range(10):
    x = random.gauss(200, 20)
    y = random.gauss(200, 20)
    data_points.append(DataPoint(x, y, "salmon", SALMON_COLOR))

# Generate 10 "sea bass" data points
for _ in range(10):
    x = random.gauss(400, 20)
    y = random.gauss(200, 20)
    data_points.append(DataPoint(x, y, "sea bass", SEA_BASS_COLOR))

# Create a new sample at position (240, 150) with no class label
new_point = DataPoint(240, 150, None, NEW_POINT_COLOR)

# Initialize kNN classifier
knn = KNNClassifier(k=3)

# Run Pygame loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Draw all the data points
    for point in data_points:
        point.draw(screen)

    # Draw the new point
    new_point.draw(screen)

    # Classify the new point using kNN and print the result
    new_point_class = knn.classify(new_point, data_points)
    print(f"The new point at (240, 150) is classified as: {new_point_class}")

    # Update Pygame display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
