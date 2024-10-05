import pygame
import random
import math

# Exercise 2: Make a class to contain a data point.
class Data_point:
    def __init__(self, position, label, color):
        self.position = position
        self.label = label
        self.color = color

    # Exercise 4: Add a draw method.
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, 5)


# Exercise 8: Implement the KNN algorithm.
class KNN:
    def __init__(self, data_points):
        self.data_points = data_points

    def classify(self, unknown_sample, k):
        # Find distances to all points:
        distances = []
        for point in self.data_points:
            distances.append((self.compute_distance(point, unknown_sample),
                              point.label))
        
        # Sort the distances and find the k nearest neighbors:
        distances.sort(key=lambda x: x[0])
        k_nearest = distances[:k]

        # Count the labels among the k nearest neighbors:
        votes = {}
        for distance, label in k_nearest:
            if label not in votes:
                votes[label] = 1
            else:
                votes[label] += 1

        # Find the label with the most votes:
        votes = list(votes.items())
        votes.sort(key=lambda x: x[1], reverse=True)
        return votes[0][0]

    def compute_distance(self, sample1, sample2):
        return math.sqrt((sample1.position[0] - sample2.position[0])**2 +
                         (sample1.position[1] - sample2.position[1])**2)


def main():
    screen = initialize_pygame()

    # Exercise 3: Instantiate 10 data points in a list.
    data_points = []
    for _ in range(10):
        sample = Data_point((random.gauss(200, 20), random.gauss(200, 20)),
                            "salmon", 
                            (255, 0, 0))
        data_points.append(sample)

    # Exercise 5: Add 10 new data points to the list.
    for _ in range(10):
        sample = Data_point((random.gauss(400, 20), random.gauss(200, 20)),
                            "sea bass", 
                            (0, 0, 255))
        data_points.append(sample)

    # Exercise 7: Add and draw an unknown sample.
    unknown_sample = Data_point((240, 150),
                                "unknown", 
                                (0, 255, 0))
    unknown_sample.draw(screen)

    # Exercise 4+6: Draw data points.
    for data_point in data_points:
        data_point.draw(screen)

    # Exercise 9: Instantiate a KNN object and classify the unknown sample.
    knn = KNN(data_points)
    class_of_unknown = knn.classify(unknown_sample, 3)
    print(f"The unknown sample is a {class_of_unknown}.")

    game_loop()


def initialize_pygame():
    pygame.init()
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My Pygame Window")
    screen.fill((255, 255, 255))
    return screen


def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()