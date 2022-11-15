import pandas as pd

data = pd.read_csv(r'C:\Pythoncode\Giants.csv')
print(data)
df = pd.DataFrame(data, columns=['CEO','DATA'])
print(df)