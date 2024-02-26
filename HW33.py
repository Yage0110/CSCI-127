#Name:  Agyei Bacchus
#Email: agyei.bacchus92@myhunter.cuny.edu
#Splice a logo


import matplotlib.pyplot as plt
import numpy as np

file = input('Enter filename:')
out = input('Enter output filename:')
img = plt.imread(file) 
height = img.shape[0]
width = img.shape[1]
img2 = img[height//2: , :width//2]


plt.imsave(out, img2)




