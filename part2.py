import pandas as pd
import numpy as np

def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

bi = pd.read_csv(r'supera-data-test\test.csv')

df = bi

df['pr_domreturn'] = df['domgross_2013']/df['budget_2013']
df['pr_intreturn'] = df['intgross_2013']/df['budget_2013']

rt_dom = df['pr_domreturn'].describe()['50%']
rt_int = df['pr_intreturn'].describe()['50%']

df['mdb_dom'] = np.where(df['pr_domreturn'] >= rt_dom, 1, 0)
df['mdb_int'] = np.where(df['pr_intreturn'] >= rt_int, 1, 0)
df['mdb'] = np.where(df['mdb_dom']+df['mdb_int']>0, 1, 0)

print(df)
print(df['mdb'].describe())

bf = df.drop(['pr_domreturn','pr_intreturn','mdb_dom','mdb_int'], axis=1)
print(bf)

bf.to_csv(r'supera-data-test\teste_retunr.csv',index=False)