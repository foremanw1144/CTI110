# William Foreman
# September 23, 2018
# CTI-110-0901 P2HW2
# Celsius/Fahrenheit Converter
# P2HW2 - P2HW2_MaleFemale_Percentage_FirstLast.py 
#
#The first line will ask the user for the number of males in the class
#and will assign that number to the variable 'males'
males = int(input("Please enter the number of males in the class: "))
#The second line will ask the user for the number of females in the class
#and assign that number to the variable 'females'
females = int(input("Please enter the number of females in the class: "))
#This line will take the variable 'males' and add it to the variable
#females and assign that number to the variable 'totalStudents'
totalStudents = males + females
#This line will divide the variable 'totalStudents' by the variable
#'males' and assign that number to the variable 'malePercentage'
malePercentage = males/totalStudents
#This line will divide the variable 'totalStudents by the variable
#'females' and assign that number to the varable 'femalePercentage'
femalePercentage = females/totalStudents
#This line is one single command broken into 3 lines to not exceed 80
#characters and will print out the total number of students and the
#percentage of males and the percentage of females
print("There are " + str(totalStudents) + " students in the class. " + \
      format(malePercentage, ".0%") + " of them are males and " + \
      format(femalePercentage, ".0%") + " of them are females")
