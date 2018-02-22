# Hypothesis:
# In a population of players with equal likelihood of winning a tournament (i.e., placement is due to pure chance), the Gini Coefficient of the rankings would have a low expected value, very close to zero.

# This code is a Monte Carlo simulation for Gini Coefficients for the 'top' 100 tennis players in a theorical population of 128 players, all of whom are equally skilled.  As a result, random chance governs the results of tournaments.

# The results are based on a model wherein:
#   – all players play each week
#   – there is only 1 tournament each week
#   – the points are awarded as in an ATP 1000
# (or maybe just 1 to 100? 128? rather than ATP, for simplicity?)

# First we run 51 weeks to produce the first starting 'complete' trailing-12-month ranking.

# Then we run our simulation: in this case 10k weeks. The Gini Coefficient for each of the 52-week rankings is calculated and the results averaged to give an estimate of the expected value of the Gini Coefficient for a population of equally matched players.

# The Gini Coefficient charts are then plotted on a single chart to help visualize the dispersion.  The mean, median, mode, and standard deviation of the data set are reported as an estimate of the expected value.

# Create dictionary for {tournament place : ranking points}. This would allow different point schemes. Better to use function based on (2 ** x) to define indexes?

points = {
            1:1000;
            2:600;
            3:360; 4:360;
            5:180; 6:180; 7:180; 8:180;
            9:90; 10:90; 11:90; 12:90; 13:90; 14:90; 15:90; 16:90;
            17:45; 18:45; 19:45; 20:45; 21:45; 22:45; 23:45; 24:45; 25:45; 26:45; 27:45; 28:45; 29:45; 30:45; 31:45; 32:45; 33:45; 34:45; 35:45; 36:45;

            }

FW 1000
FL 600
SLs 360
QLs 180
R16Ls 90
R32Ls 45
R64Ls 25
R128Ls 10

# Create dataframe for 128 players, results by week, Gini for each week.



# Assign random places for 10051 tournaments to players using seeds 1–10051; append.



# Calculate Gini for each week; append.



# Calculate Gini-weighted rank for each player for each full-ranking week; create
# new dataframe.



# Calculate cumulative Gini-weighted ranking for each player; append.



# Create Gini plot for all weeks; include mean, median, mode, std dev for full weeks.
