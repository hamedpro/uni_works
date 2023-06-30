import numpy as np
import pandas as pd 
import seaborn as sb 
from pprint import pprint
import matplotlib.pyplot as mp
import sklearn
def calc_unique_pairs(list):
    results = []
    for i in list:
        for j in list:
            if (not [i,j] in results) and (not [j,i] in results):
                  results.append([i,j])
    return results
df = pd.read_csv('Dry_Bean.csv')

cols = df.drop(columns=['Class']).columns
results = {}


for col in cols :
    results[col ] = {}
    results[col]['mean'] = np.mean(df[col])
    results[col]['standard_deviation'] = np.std(df[col])
    results[col]['min'] = np.min(df[col])
    results[col]['q1'] = np.percentile(df[col] , 25)
    results[col]['q2'] = np.percentile(df[col] , 50)
    results[col]['q3'] = np.percentile(df[col] , 75)
    results[col]['max'] = np.percentile(df[col] , 100)
    results[col]['count'] = np.count_nonzero(df[col])
    results[col]['sum'] = np.sum(df[col])

correlation_matrix = df.drop(columns=['Class']).corr()
#print(correlation_matrix)

columns = df.columns[:-1]
def calc_ceofficient(pair):
    return correlation_matrix[pair[0]][pair[1]]
unique_pairs = calc_unique_pairs(columns) # [i1 , i2 , i3]
unique_pairs_ceofficients = [calc_ceofficient(pair) for pair in unique_pairs] # [0,8 , 1 , 0.5]

selected_pairs = [pair  for pair in unique_pairs if calc_ceofficient(pair) > 0.8 ]
selected_pairs_ceofficients = [calc_ceofficient(pair) for pair in selected_pairs]


df2 = pd.DataFrame({"pair" : selected_pairs , "correlation_ceofficient"  : selected_pairs_ceofficients})

#task 3
dataplot = sb.heatmap(correlation_matrix)
#mp.show()


#task 4 

onehot_encoded = pd.get_dummies(df)