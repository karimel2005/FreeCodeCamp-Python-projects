import copy
import random


class Hat:
    
    def __init__(self, **colors):
        self.colors = colors
        self.contents = []

        # fill contents
        for color, num in colors.items():
            for i in range(num):
               self.contents.append(color)

    def __str__(self):
        return str(self.colors)
    
    def draw(self, num_to_draw):
        ball_list = []
        if num_to_draw > len(self.contents):
            for i in range(len(self.contents)):
                rand = random.choice(self.contents)
                ball_list.append(rand)
                self.contents.pop(self.contents.index(rand)) 
        else:
            for j in range(num_to_draw):
                rand = random.choice(self.contents)
                ball_list.append(rand)
                self.contents.pop(self.contents.index(rand))
        
        return ball_list

 
    
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    # turn expected_balls to list in order to check it with each draw
    exp_balls = []
    for color, num in expected_balls.items():
        for i in range(num):
           exp_balls.append(color)

    for experiment_ in range(num_experiments):
        count = 0
        hat1 = copy.deepcopy(hat)
        draw = hat1.draw(num_balls_drawn)
        for ball in exp_balls:
            if ball in draw:
                count += 1
                draw.pop(draw.index(ball))
        if count == len(exp_balls):
            success += 1


    prob = success / num_experiments
    return prob


# Testing Zone (keep out)

hat1 = Hat(black=6, red=4, green=3)
#print(hat1.draw(2))
#print(hat1.contents)
expected_balls = {'red':2,'green':1}
experiment_Alpha = experiment(
    hat1, 
    expected_balls, 
    5, 
    2000)

print(experiment_Alpha)