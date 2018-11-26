#William Foreman
#CTI-110-0902
#Python 3 Shipping Charges
#10/16/2018
#
#
#Ask the user for the weight of the package.
packageWeight = int(input("What is the weight of your package?  "))

#Use if elif else statement to compare rates for package weights.
if packageWeight <= 2:
	charge = 1.50
elif packageWeight <= 6:
	charge = 3.00
elif packageWeight <= 10:
	charge = 4.00
else:
	charge = 4.75

#Print the price of the package being sent.
print("It will cost you $" + format(charge, ",.2f") + " for a package \n"
      "with a weight of " + str(packageWeight) + "oz.")