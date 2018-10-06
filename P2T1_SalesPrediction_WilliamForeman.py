# William Foreman
# September 23, 2018
# CTI-110-0902 P2T1-Sales Prediction
# Predicts the amount of profit from the total sales
# The value 0.23 will represent 23 percent
#
# This line assigns the user input as the variable for projected total sales
projectedTotalSales = float(input("Please enter the projected amount of total sales: $"))
# This line is our equation to find the profit from the % of total sales
profit = 0.23 * projectedTotalSales
# This line prints the profit
print("The projected profit will be $" + format(profit , ",.2f"))
