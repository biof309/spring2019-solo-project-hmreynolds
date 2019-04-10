
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
print(fifa1.loc)
print(fifa1.info())

fifa1.columns.get_loc('Nationality')
fifa1.columns.get_loc('Age')
Nat_Age = fifa1.iloc[[3]]
print(Nat_Age)



y_col = fifa1[fifa1['Age'] > 45]
fifa1.plot(x='Nationality', y=y_col)
plt.show()

