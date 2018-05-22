# This is a Monte Carlo simulation to estimate the expected Gini coefficient for 100 equal actors' accumulated points over a set number of plays.

import numpy as np
import random as rd

rd.seed(1)

# Create a key of 100 players
players = [[i for i in range(1000000, 1000100)]]
np_player_key = np.array(players)

# Create list of 100 possible scores
scores = [i for i in range(100)]
temp_scores = [scores]
np_temp = np.array(temp_scores)

# Create results array
np_results = np.append(np_player_key, np_temp, axis = 0)

# Shuffle scores, create np score array, and append
for i in range(130):
    rd.shuffle(scores)
    x = [scores]
    np_scores = np.array(x)
    np_results = np.append(np_results, np_scores, axis = 0)

# Delete non-randomized score set
np_results = np.delete(np_results, 1, 0)
