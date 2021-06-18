import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'supera-data-test\bechdel.xlsx', sheet_name='bechdel', usecols="A,C,E,G,H,I,J", skiprows=[0])

g = df['binary']
perc = pd.concat([g.value_counts(), 
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
print('Total e percentual aprovação:')
print (perc)

g = df.groupby('year')['binary']
percy = pd.concat([g.value_counts(), 
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))

print('Percentual de aprovação ao longo do tempo:')
print (percy)

final = df.groupby(['year','binary'])['binary'].count().reset_index(name="count")
piv = final.pivot(index="year", columns="binary", values="count")

axis = piv[["PASS", "FAIL"]].plot(kind="bar", stacked=True)
axis.set_ylabel('Total Aprovação/Reprovação')
axis.set_xlabel('Tempo')
axis.set_title('Total de aprovação de filmes pelo teste Bechedel')
axis.legend()
fig = axis.get_figure()

plt.show()