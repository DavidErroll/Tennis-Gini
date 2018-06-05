
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

def aggregate_play(players, rounds, samples):

    # Create sums array
    sums_list = [i for i in range(players)]
    np_sums = np.array([sums_list])

    for s in range(samples):
        np_sample = single_play(players, rounds)
        temp_sums = [np.sum(a = np_sample, axis = 0)]
        np_sums = np.append(arr = np_sums, values = temp_sums, axis = 0)

    # Delete non-randomized score set
    np_sums = np.delete(arr = np_sums, obj = 0, axis = 0)

    return(np_sums)





# The interface function allows the user to set the input parameters: (1) number of players; (2) number of rounds per iteration; and (3) the number of iterations. For the standard model here, we use

# (1) 100 players, 1 player per one-percent bin in Lorenze curve;
# (2) 30 rounds per iteration, for a basically statistically significant sample size; and
# (3) 10,000 iterations, for a large Monte Carlo simulation base.


def interface():
    players_in = int(input("Number of players = "))
    rounds_in = int(input("Number of rounds per iteration = "))
    samples_in = int(input("Number of iterations = "))

    np_results = aggregate_play(players_in, rounds_in, samples_in)

    print(np_results)


def main():
    interface()

main()
