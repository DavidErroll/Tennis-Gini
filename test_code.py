import numpy as np
import pandas as pd
from sklearn.utils import shuffle

# Create list for {tournament place : ranking points}. This would allow different point schemes.

df_point_list = pd.DataFrame([1000] + [600] + [360] * 2 + [180] * 4 + [90] * 8 + [45] * 16 + [25] * 32 + [10] * 64)

df_scores = pd.DataFrame(x for x in range(1, 129))

df_2 = shuffle(df_point_list)

pd.concat([df_scores, df_2], axis = 1)
