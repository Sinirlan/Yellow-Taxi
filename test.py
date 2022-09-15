import pandas as pd
 
# read DataFrame
data = pd.read_csv("Customers.csv")
 
for (gender), group in data.groupby(['Gender']):
     group.to_csv(f'{gender}.csv', index=False)
 
print(pd.read_csv("Male.csv"))
print(pd.read_csv("Female.csv"))