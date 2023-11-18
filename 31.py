import pandas as pd
import matplotlib.pyplot as plt



file = input('Enter file name:')
out = input('Enter output name:')


homeless = pd.read_csv("DHS_Daily_Report.csv")
homeless.plot(x = "Date of Census", y = "Total Individuals in Shelter")
plt.show()