import pandas as pd 
import numpy as np 
import pprint
df = pd.read_csv('Dry_Bean.csv')

results ={}
results['means'] = list(map(lambda col : np.mean(df[col]), df.columns[:-1 ]))

results['standard_deviations' ] = list(map(lambda col : np.std(df[col]), df.columns[:-1 ]))

results['min' ] = list(map(lambda col : np.min(df[col]), df.columns[:-1 ]))
results['q1' ] = list(map(lambda col : np.percentile(df[col],25), df.columns[:-1 ]))
results['q2' ] = list(map(lambda col : np.percentile(df[col],50), df.columns[:-1 ]))
results['q3' ] = list(map(lambda col : np.percentile(df[col],75), df.columns[:-1 ]))
results['max' ] = list(map(lambda col : np.max(df[col]), df.columns[:-1 ]))
results['count' ] = list(map(lambda col : np.count_nonzero(df[col]), df.columns[:-1 ]))
results['sum' ] = list(map(lambda col : np.sum(df[col]), df.columns[:-1 ]))

pprint.pprint(results )
