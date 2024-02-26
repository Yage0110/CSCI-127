# Agyei Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Programs that prints borough stats 

import pandas as pd
import matplotlib.pyplot as plt


borough = input("Enter bourough name: ")



pop = pd.read_csv('nycHistPop.csv', skiprows=5)
avg = pop[borough].mean()
pmax = pop[borough].max()
print("Average population: ", avg)
print("Max population:", pmax)

