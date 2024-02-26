# Agyei Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Programs that creates a borough graph 

import matplotlib.pyplot as plt
import pandas as pd


borough = input("Enter borough name: ")
output = input("Enter output name: ")


pop = pd.read_csv(‘nycHistPop.csv’, skiprow=5)
print(pop)

pop['Fraction'] = pop[borough] / pop['Total']
pop.plot(x="Year", y='Fraction')

plt.show()
fig = plt.gcf()
fig.savefig(output)
