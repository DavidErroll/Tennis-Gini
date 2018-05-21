# This is a Monte Carlo simulation to estimate the expected Gini coefficient for 100 equal actors' accumulated points over a set number of plays.

# Create list of 100 players

player = 'player_'
player_list = [[player + 'i'] for i in range(100)]

# Create randomizable list of possible scores

scores = [[i] for i in range(1, 100)]

# Create randomized score result

import random
random.seed(1)

random_scores = shuffle(scores)

results_list = player_list.append(random_scores)
