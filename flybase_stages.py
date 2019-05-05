#Import relevant modules 
import pandas as pd
import matplotlib.pyplot as plt

#Define variables filename and genename
filename = 'gene_rpkm_report_fb_2019_02.tsv'
genename = 'FBgn0031681'

#Read in tsv file as pandas csv
#skip first 5 rows and tab delineate 
df = pd.read_csv(filename, skiprows=5, sep='\t')

#Drop rows with unnecessary data 
df = df.drop(df[df.Parent_library_name == 'BCM_1_RNAseq'].index)
df = df.drop(df[df.Parent_library_name == 'modENCODE_mRNA-Seq_tissues'].index)
df = df.drop(df[df.Parent_library_name == 'modENCODE_mRNA-Seq_treatments'].index)
df = df.drop(df[df.Parent_library_name == 'modENCODE_mRNA-Seq_cell.B'].index)
df = df.drop(df[df.Parent_library_name == 'Knoblich_Neural_Cell_RNA-Seq'].index)

#Extract columns of interest from data set as RNAseq
RNAseq = df[['FBgn#', 'RNASource_name', 'RPKM_value']]

#Define a function that locates data rows with gene of interest and return a Dataframe
def find_gene(genename):
    df = RNAseq.loc[RNAseq['FBgn#'] == genename]
    return df

#Utilize function to generate Dataframe: data that contains gene of interest
data = find_gene(genename)
print(data.head)

#Plot data as a bar graph with stage as x-axis and RPKM values as y-axis, include genename in the legend
data.plot(kind='bar', x= 'RNASource_name', y= 'RPKM_value', color='g')
plt.xlabel('Stage')
plt.ylabel('RPKM expression')
plt.gca().legend(genename)
plt.title('RNAseq expression data for various stages of Drosophila development')

plt.show()

#Plot data as pie chart
plt.pie(data['RPKM_value'], labels=data['RNASource_name'])
plt.axis('equal')
plt.show()





