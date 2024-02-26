#Name:  Agyei Bacchus
#Email: agyei.bacchus92@myhunter.cuny.edu
#Creates a shelter census


import pandas as pd
import matplotlib.pyplot as plt

abc = input("Enter file name:")
output = input("Enter png file name: ")


homeless = pd.read_csv(abc)
homeless['FractionChildren'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
xyz = homeless.plot(x = "Date of Census", y = 'FractionChildren')
plt.show()
fig = plt.gcf()
fig.savefig(xyz)
