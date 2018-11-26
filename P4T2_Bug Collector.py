#William Foreman
#CTI-110-0902
#Python 4 Bug Collector
#10/16/2018
#
#
days = 5
totalBugs = 0

# for loop with target variable using in range command doesn't include
# the last number so days plus 1 equals 6 but the counter will stop at
# day 5
for currentDay in range(1, days + 1):
	dailyBugs = int(input("How many bus were collected on day " + \
	                str(currentDay) + ": "))
	totalBugs += dailyBugs

#Here we will print the total number of bugs collected for 5 days.
print("\nThe total number of bugs collected for", days, "days is", totalBugs)
