import copy
import random
# Consider using the modules imported above.

class Hat:
  """Initializer"""
  def __init__(self, **kwargs):
    self.contents = []
    for key, val in kwargs.items():
      while val > 0:
        self.contents.append(key) 
        val -= 1

  def draw(self, num_draw):
    if num_draw >= len(self.contents):
      return self.contents
    else:
      removed = []
      for i in range(num_draw):
        removed.append(random.choice(self.contents))
        self.contents.remove(removed[-1])
      return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
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



