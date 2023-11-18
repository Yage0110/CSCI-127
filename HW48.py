#Jay Bacchus
#Email: agyei.bacchus92@myhunter.cuny.edu
#Empty string check 


xyz = input('Enter a non-empty string: ')
while len(xyz)==0:
    print('That was empty.  Try again.')
    xyz = input('Enter a non-empty string: ')
print('You entered:', xyz)