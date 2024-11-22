import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [color for (color, number) in kwargs.items() for _ in range(number)]
        self.no_balls = len(self.contents)

    def draw(self, number):
        if number >= self.no_balls:
            draws = self.contents
            self.no_balls = 0
            self.contents = []
            return draws

        draws = []
        for _ in range(number):
            draw = random.choice(self.contents)
            draws.append(draw)
            self.contents.remove(draw)
        self.no_balls -= number

        return draws

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draws = hat_copy.draw(num_balls_drawn)
        M += all(draws.count(color) >= number for (color, number) in expected_balls.items())

    return M/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':1,'green':1},
                  num_balls_drawn=3,
                  num_experiments=2000)

print(probability)