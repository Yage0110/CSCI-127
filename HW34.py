# Agyei Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Programs that splits names
def name_organizer():
    names_input = input("Please enter your list of names: ")
    names_list = names_input.split('; ')

    print("You entered:")
    for name in names_list:
        last_name, first_name = name.split(', ')
        print(first_name,last_name)

    print("Thank you for using my name organizer!")

name_organizer()
