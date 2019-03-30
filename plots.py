import pandas
from collections import defaultdict
from matplotlib import pyplot as plt


df=pandas.read_csv("InfoMediaworld.csv", sep=';')
name = df.columns.values
file = open("results.txt",'w+')
column = df['Column4']
#print(len(column))
dict = defaultdict(int)
for value in column:
    dict[value]+=1
keys = sorted(dict)
values = []
for key in keys:
    values.append(dict[key])
    file.write(str(key)+"\t"+str(dict[key])+"\n")
#plt.plot(keys , values, 'b', label='Tags Tot')
#plt.show()