#William Foreman
#CTI-110-0902
#Python 5 Feet to Inches
#10/16/2018
#
#
# Need to define a function to multiply the number of feet by the number of
# inches per foot. 
def ftToIn( userInputFt ):
    inches = ( userInputFt * 12 )
    return inches

#Define the main function which will ask our user for the number of feet
#to convert to inches, and print the result.
def main():
    userInput = float(input( "Please enter the number of feet you want to"
                             "convert to inches: "))
    inches = ftToIn( userInput )
    print()
    print( userInput, "feet converted to inches is"
           ,format(inches, ",.3f"), " inches." )
main()