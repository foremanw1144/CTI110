#William Foreman
#CTI-110-0902
#Python 5 Kilometer Converter
#10/16/2018
#
#
#The formula is M = KM x 0.6214
#Functions don't see each other so variable names can be the same.
#Define a function that asks the user for the number of KMs. Use the float
#statement so we can use a decimal if the distance isn't a whole number.
def askUserForKilometers():
    userKilometers = float(input("Please enter the distance in kilometers: "))
    return userKilometers

#Define a function to convert the user given KMs to miles using the above
#mentioned equation.
def convertToMiles( kilometers ):
    miles = kilometers * 0.6214
    return miles

#Define the main function to pull it all together and print out the resulting
#number of miles from the given number of KMs.
def main():
    userInput = askUserForKilometers()
    miles = convertToMiles( userInput )
    print()
    print(userInput, " Kilometers is" ,format(miles, ",.2f"), " Miles.")
main()