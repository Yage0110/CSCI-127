# Jay Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Program that colors the image blue


import matplotlib.pyplot as plt
import numpy as np

input_file = input("Enter input image name: ")
output_file = input("Enter output image name: ")

img = plt.imread(input_file)

img2 = img.copy()
img2[:,:,1] = 0
img2[:,:,0] = 0
plt.imsave(output_file, img2)
print(output_file)
