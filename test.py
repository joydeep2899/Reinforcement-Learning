import pandas as pd

i=0
df=pd.DataFrame(columns=[0,1])

a=pd.Series([4]*2,index=[0,1],name='state')
#for i  in  range(2):
print(a)
df.append(a,ignore_index=True)
print(df)

a=[]
#for j in a.index:
#   print(a[j])