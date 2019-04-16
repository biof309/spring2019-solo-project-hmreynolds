from zipfile import ZipFile
transgene = "construct_maps.zip"
with ZipFile(transgene, 'r') as zip:
    zip.printdir()
    zip.extractall()
import pandas as pd
import matplotlib as plt
flybase = pd.read_csv(transgene)
print(flybase[0].head())