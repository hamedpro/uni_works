import numpy as np 
import pandas as pd

df =  pd.DataFrame({"ages" : [i for i in range(10,40)]})

print(np.percentile(df['ages'] , 25))