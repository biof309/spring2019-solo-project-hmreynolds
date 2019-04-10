
from zipfile import ZipFile
fifa = "fifa19.zip"
with ZipFile(fifa, 'r') as zip:
    zip.printdir()
    zip.extractall()
import pandas as pd
import matplotlib.pyplot as plt
fifa1=pd.read_csv(fifa)
print(fifa1.head(10))
print(fifa1.keys())
print(fifa1.info())

fifaNA = fifa1[['Nationality','Age']]
print(fifaNA)

Group = fifaNA.groupby(['Nationality'], as_index=True).agg('mean')
print(Group)

Nat = fifaNA[['Nationality']]
Nat_drop = Nat.drop(axis=0)
print(Nat_drop)

Group_graph = Group.reset_index().plot(x='Nationality', y='Age')
plt.xlabel('Nationality')
plt.ylabel('Mean Age')
plt.show()

