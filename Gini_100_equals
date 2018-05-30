# The basic premise is estimating an expected Gini coefficient for the results of repeated game play among participants that are equally skilled – i.e., equally likely to finish any given game play event in any of 100 places.

# This Monte Carlo simulation code creates a 30-play total for 100 players that have been randomly assigned scores of 0 to 99.  This process is then iterated 10,000 times.

# For each of the Gini percentiles, we calculate the arithmetic mean (μ) and standard deviation (σ) of the 10,000 samples. We then plot Lorenze curves for: (1) each 30-play result (gray); (2) the curve of mean values (solid black); and (3) the upper and lower limits of a confidence band connecting the points at μ ± 2σ (broken black).

import numpy as np
import random as rd

rd.seed(1)

def play_rounds(rounds):

  # Create list of 100 possible scores (0 to 99)
  scores = [i for i in range(100)]
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
  np_results = np.delete(arr = np_results, obj = 1, axis = 0)

  return (np_results)

def
