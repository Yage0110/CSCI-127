# Agyei Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Programs for parking tickets
import pandas as pd
filename = input('Enter file name:')
data = pd.read_csv(filename)
attribute = input('Enter attribute:')
top_offenders = data[attribute].value_counts().head(10)
print("The 10 worst offenders are:")
print(top_offenders)
print('Name:',attribute, 'dtype:int64')
