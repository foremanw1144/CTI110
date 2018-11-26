#William Foreman
#CTI-110-0902
#Python 4 Celsius to Fahrenheit Table
#10/16/2018
#
#
# Fahrenheit to Celsius formula is:
# F = ( 9 / 5 ) C + 32
#
#This is a table no need for user input. Create a title line and create
#a couple of column header titles. One for the Celsius Temp and one for
#the Fahrenheit Temp.
print("We will now convert some Celsius Temperatures to Fahrenheit!!")
print()
print("Celsius Temperature \t Fahrenheit Temperature")
print("------------------- \t ----------------------")

#Use a for loop with a range of 0 to 21 for my temperatures to be converted.
#Use a method to center the temperatures under the column headers ie \t, ljust
#or "    ".
for curCelTemp in range(0, 21):
    fahrenheitEquvalent = ((9/5) * curCelTemp) + 32
    print("\t",curCelTemp,"\t\t" + "    ",format(fahrenheitEquvalent, ",.2f"))

