# Jay Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Program that prints snow count

import numpy as np
import matplotlib.pyplot as plt

ca = plt.imread(input("Enter file neame:"))

countSnow = 0
t=0.75

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0]> t) and (ca[i,j,1]> t) and (ca[i,j,2]> t):
            countSnow = countSnow +1
print ("Snow count is", countSnow)