#William Foreman
#CTI-110-0902
#Python 3 Roman Numerals
#10/16/2018
#
#
#Request a number between 1 and 10 from the user and assign that number to
#the variable called number.
number = int(input("Please enter an english number between 1 and 10. "))

#Need to handle errors for numbers outside the range of 1 thru 10 as well as
#translate the english number to the corresponding roman numeral.
#Use an if elif else statement to translate the english number to a roman
#numeral
if number == 1:
	print("The roman numeral for", number, "is I.")
elif number == 2:
	print("The roman numeral for", number, "is II.")
elif number == 3:
	print("The roman numeral for", number, "is III.")
elif number == 4:
	print("The roman numeral for", number, "is IV.")
elif number == 5:
	print("The roman numeral for", number, "is V.")
elif number == 6:
	print("The roman numeral for", number, "is VI.")
elif number == 7:
	print("The roman numeral for", number, "is VII.")
elif number == 8:
	print("The roman numeral for", number, "is VIII.")
elif number == 9:
	print("The roman numeral for", number, "is IX.")
elif number == 10:
	print("The roman numeral for", number, "is X.")

#Create the error handling exception with an else statement and print a
#message to the user letting them know what happened.
else:
	print("Error: Please enter a number between 1 and 10.")