# Agyei Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Program that prints red and white stripes



import matplotlib.pyplot as plt
import numpy as np
num = int(input("Enter size: "))


output_img = input("File name: ") 
img = np.ones((num,num,3))
img[::2,:,1 ]=0
img[::2,:,2 ]=0

plt.imsave(output_img, img)
