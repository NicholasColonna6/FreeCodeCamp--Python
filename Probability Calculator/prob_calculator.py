# Nick Colonna

import copy
import random

class Hat:
    """ A class to simulate a hat containing balls of different colors for probability experiments

        Attributes:
        **kwargs -- dictionary allowing for variable number of parameters containing color and number of balls [ie: Hat(red=5, blue=2)]

        Methods:
        draw(num_draw) -- removes a specified number of balls from the Hat without replacing
    """ 
    def __init__(self, **kwargs):
        """Initializer -- adds all balls specified into the hat"""
        self.contents = []
        for key, val in kwargs.items():
            while val > 0:
                self.contents.append(key) 
                val -= 1

    def draw(self, num_draw):
        """
            Draw specified number of balls from the Hat without replacing.
            Return list of all balls removed
        """
        if num_draw >= len(self.contents):
            return self.contents
        else:
            removed = []
            for i in range(num_draw):
                removed.append(random.choice(self.contents))
                self.contents.remove(removed[-1])
            return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """ Runs an experiment to return the probability of picking 'expected_balls' from a hat while drawing 'num_balls_drawn'

        Parameters:
            hat -- Hat object containing balls
            expected_balls -- object indicating exactly what we are trying to draw from the hat (ex: {"blue":2, "red":1})
            num_balls_drawn -- number of balls to draw with each experiement
            num_experiments -- number of experiements to perform

    """
    original_hat = copy.deepcopy(hat.contents)
    balls_expected = []
    for key, val in expected_balls.items():
        while val > 0:
            balls_expected.append(key) 
            val -= 1
      
    successes = 0
    for i in range(num_experiments):
        hat.contents = copy.deepcopy(original_hat)
        expected = copy.deepcopy(balls_expected)
        drawn_balls = hat.draw(num_balls_drawn)
        for ball in drawn_balls:
            if ball in expected:
                expected.remove(ball)
                if expected == []:
                    successes +=1
                    break
      
    return successes / num_experiments



