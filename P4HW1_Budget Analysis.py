#William Foreman
#CTI-110-0902
#Python 4 Budget Analysis
#10/16/2018
#
#
# Request user to input an amount of money since this could be dollar and cents
# we will need to use the float command to use decimal places.
budgetedMoney = float(input("Please enter the amount you have budgeted for "
                            "the month $"))
additionalExpense = "y"
totalExpense = 0

#Use a while if elif else statement to loop if there there are expenses and how
#much each expense is. Also print a statement letting the user know if they
#stayed within their budget or not and by how much.
while additionalExpense == "y":
    personalExpense = float(input("\nEnter an expense $"))
    totalExpense += personalExpense
    additionalExpense = input("\nIs there another expense?: Type y for yes or"
                              "n for no: ")
if totalExpense > budgetedMoney:
    print("\nYou busted your budget of $",format(budgetedMoney, ",.2f"),"by $"
          ,format(totalExpense - budgetedMoney, ",.2f"))
elif totalExpense < budgetedMoney:
    print("\nYou did great! You were under your budget of $"
          ,format(budgetedMoney,",.2f"),"by $"
          ,format(budgetedMoney - totalExpense,",.2f"))
else:
    totalExpense == budgetedMoney
    print("\nNot bad. You didn't exceed your budgeted amount of $"
          ,format(budgetedMoney, ",.2f"))
#
#It's really annoying but I can't seem to figure out how to get rid of the
#in the output between the $ and the first number.