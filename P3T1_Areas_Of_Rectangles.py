#William Foreman
#CTI-110-0902
#Python 3 Areas of Rectangles
#10/16/2018
#
#

#Here we will have the user input the length and width of the rectangle and
#assign those inputs to variables to use in the equation to fine areas of
#objects i.e. length times width.
recLen1 = float(input("Please enter the length of the first rectangle: "))
recWid1 = float(input("Please enter the width of the first rectangle: "))
recLen2 = float(input("Please enter the length of the second rectangle: "))
recWid2 = float(input("Please enter the width of the second rectangle: "))

#Do the area equation and assign the result to a variable to be used later.
recArea1 = recLen1 * recWid1
recArea2 = recLen2 * recWid2

#Use an if else statement to output to the user which rectangle is bigger and
#give them the size. We won't use an actual measurement type since the user
#could use metric or imperial and we aren't trying to convert anything.
if recArea1 > recArea2:
        print("The area of the first rectangle is",recArea1, "and is bigger \n"
              "than the second rectangle.")
elif recArea1 < recArea2:
	print ("The area of the second rectangle is",recArea2, "and is bigger \n"
               "than the first rectangle.")

#Explicitly state both rectangles are equal with either an elif or else
#statement 
elif recArea1 == recArea2:
	print ("The areas of the rectangles are",recArea1 + recArea2, "and are \n"
               "the same.")
