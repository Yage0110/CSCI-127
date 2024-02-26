# Agyei Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Program that encrypts a message
Word = input("Enter a word: ")
code = ""
for i in Word:
    newCode = chr((ord(i) - ord('a') + 13) % 26 + ord('a'))
    code += newCode
print("Your code is:", code)

