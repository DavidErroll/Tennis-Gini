# This is a Monte Carlo simulation to estimate the expected Gini coefficient for 100 equal actors' accumulated points over 100 rolling samples of 30 plays.

import numpy as np
import random as rd

rd.seed(1)

total_samples = 100

# Create a key of 100 players
#players = [[i for i in range(1000000, 1000100)]]
#np_player_key = np.array(players)

# Create list of 100 possible scores
scores = [i for i in range(100)]
temp_scores = [scores]
np_temp = np.array(temp_scores)

# Create results array
np_results = np.append(np_player_key, np_temp, axis = 0)

# Shuffle scores, create score array, and append
for i in range(total_samples + 30):
    rd.shuffle(scores)
    x = [scores]
    np_scores = np.array(x)
    np_results = np.append(np_results, np_scores, axis = 0)

# Delete non-randomized score set
np_results = np.delete(np_results, 1, 0)

# Create array of rolling totals
for j in range(total_samples):
    rolling_sum = [sum(np_results[j:j+30], 0)]
    if j == 0:
        np_rolling_sums_30 = rolling_sum
    else:
        np_rolling_sums_30 = np.append(np_rolling_sums_30, rolling_sum, axis = 0)
