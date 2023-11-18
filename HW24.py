# Jay Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Programs that counts plurals

nouns= (input("Enter a list of nouns:"))
print(nouns)
abc = nouns.split(" ")

nums = len(abc)
print("Number of words:",nums)
word = nouns.count("s ")
ggg = nouns[:-1].split("s")
www = len(ggg)
print("Fraction of your list that is plural is:", word/nums)