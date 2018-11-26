#William Foreman
#CTI-110-0902
#Python 4 Tuition Increase Calculator
#10/16/2018
#
#
#Print a title to the table. Make two columns with titles.
#First title is Year second title is Tuition.
print("This will calculate the tuition for the next 5 years")
print()
print("Year \t  Tuition")
print("----- \t----------")
currentTuition = 8000

#Use a for in range loop to go through each year and calculate
#the tuition using the given formula of 3 divided by 100 times
# the current tuition.
for currentYear in range(2018, 2023):
    currentTuition += (3/100) * currentTuition
    print(currentYear, "\t$",format(currentTuition, ",.2f"))

