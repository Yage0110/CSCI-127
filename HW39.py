# Jay Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Contributing factors

import pandas as pd
filename = input('Enter filename:')
collisions = pd.read_csv(filename)
print('Top three contributing factors for collisions:')
print(collisions['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().head(3))


