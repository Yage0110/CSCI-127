# Jay Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Program that prints a substring pyramid

s = input("Enter string:")
ls = len(s)
for i in range(0,ls-1):
    print(s[0:i])
for i in range(0,ls-1):
    print(s[i:ls])
print("Thank you for using my program!")
