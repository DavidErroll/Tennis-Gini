# The basic premise is estimating an expected Gini coefficient for the results of repeated game play among participants that are equally skilled – i.e., equally likely to finish any given game play event in any of 100 places.

# This Monte Carlo simulation code creates a 30-play total for 100 players that have been randomly assigned scores of 0 to 99.  These results are then summed for each player and sorted by value, from which a Gini coefficient can be determined for that 30-play instance.

# This process is then iterated 10,000 times.

# For each of the Gini percentiles, we calculate the arithmetic mean (μ) and standard deviation (σ) of the 10,000 samples. We then plot Lorenze curves for: (1) each 30-play result (gray); (2) the curve of mean values (solid black); and (3) the upper and lower limits of a confidence band connecting the points at μ ± 2σ (broken black).

import numpy as np
import random as rd

rd.seed(1)

# The single_play function models an instance of a given number of "rounds" among a fixed number of players, where the players are ranked from first to last place (i.e., awarded points of 99 to 0) randomly because they are all of exactly equal skill; single_play produces an array of shape [number of players] x [number of rounds].

def single_play(players, rounds):

    # Create list of possible scores; here players should = 100 (0 to 99)
    scores = [i for i in range(players)]
    temp_scores = [scores]

    # Create results array
    np_results = np.array([scores])

    # Shuffle scores, create score array, and append
    for i in range(rounds):
        rd.shuffle(scores)
        x = [scores]
        np_scores = np.array(x)
        np_results = np.append(arr = np_results, values = np_scores, axis = 0)

    # Delete non-randomized score set
    np_results = np.delete(arr = np_results, obj = 0, axis = 0)

    return(np_results)

# The aggregate_play function iterates single_play, summing the results for each player across the rounds; aggregate_play produces an array of shape [number of players] x [number of samples].

def aggregate_play():
    # Create sums array
    sums_list = [i for i in range(100)]
    np_sums = np.array([sums_list])

    # Sum all scores in np_results
    temp_sums = np.sum(a = np_results, axis = 0)

print(np_results)
print(np_sums)
print(temp_sums)
