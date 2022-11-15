import pandas as pd
#using the dict data-->df
data = {'country': ['Belgium', 'India', 'Brazil'],
        'capital': ['Brussesls', 'Newdelhi', 'Brassillia'],
        'population': [11190846,1303171035,2048784652]}
df = pd.DataFrame(data,columns=['country','capital','population'])
print(df)