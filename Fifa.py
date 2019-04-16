#%% Import zipfile and extract as read-only
from zipfile import ZipFile
fifa = "fifa19.zip"
with ZipFile(fifa, 'r') as zip:
    zip.printdir()
    zip.extractall()
#%% Import pandas and matplotlib and read in zipfile as csv
import pandas as pd
import matplotlib.pyplot as plt
fifa1=pd.read_csv(fifa)
#%% Inspect data file
print(fifa1.head(10))
print(fifa1.keys())
print(fifa1.info())
#%% Identify columns of interest and isolate them from data set
fifaNA = fifa1[['Nationality','Age']]
print(fifaNA)
#%% Group by Nationality to merge identical names and aggregate to mean to find\
#%% mean age per Nationality (set Nationality to index)
Group = fifaNA.groupby(['Nationality'], as_index=False).agg('mean')
print(Group)
#%% Sort data using conditions
NAT = Group['Nationality']
AGE = Group['Age']
#%% Plot bar graph setting x- and y- axes
Group_graph = plt.scatter(NAT,AGE)
plt.xticks(rotation = 90)
plt.axes.vlines()
plt.xlabel('Nationality')
plt.ylabel('Mean Age')
plt.show()







