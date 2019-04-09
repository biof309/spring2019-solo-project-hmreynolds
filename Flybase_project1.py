
from zipfile import ZipFile
fifa = "fifa19.zip"
with ZipFile(fifa, 'r') as zip:
    zip.printdir()
    zip.extractall()
import pandas as pd
fifa1=pd.read_csv(fifa)
print(fifa1.head())

list(fifa1.columns.values)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///fifa1.sqlite')
connection = engine.connect()

import select
stmt = select([fifa1])
stmt = stmt.where(fifa1.columns.Nationality == 'American')
results = connection.execute(stmt).fetchall()
for result in results:
    print(results.Nationality, results.Name)