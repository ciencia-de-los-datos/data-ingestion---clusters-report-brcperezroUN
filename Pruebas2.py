with open('clusters_report.txt') as f:
    contents = f.readlines()

for line in contents:
    print(line)



import pandas as pd
listAnchoCols = [9, 16, 16, 76]
pd.read_fwf('clusters_report.txt', widths=listAnchoCols,  header=[0,1], skiprows=[3])

#opcion2
pd.read_fwf('clusters_report.txt', widths=listAnchoCols,  header=None, skiprows=4)

df.fillna('', inplace=True)
df = df.drop(labels = 0,axis = 1).astype(str).groupby(df[0].mask(df[0]=='').ffill()).agg(' '.join).reset_index()






df = pd.read_fwf('clusters_report.txt', widths=listAnchoCols,  header=None, skiprows=[2,3])
df.fillna('', inplace=True)
df = df.drop(labels = 0,axis = 1).astype(str).groupby(df[0].mask(df[0]=='').ffill()).agg(' '.join).reset_index()
df.columns = df.loc[13]
df.drop(13, axis=0, inplace= True)

