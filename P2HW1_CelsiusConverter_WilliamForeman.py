# William Foreman
# September 22, 2018
# CTI-110-0902 P2HW1-Celsius Fahrenheit Converter
# Celsius_Fahrenheit_Converter
# This program will convert Celsius temperatures to Fahrenheit
# The calculation used will be F=(9/5)C+32
#
#This line will ask the user for the Celsius Temperature
celsiusTemperature = float(input("Please enter a temperature in celsius: "))
#This line will give me the Fahrenheit Temperature
fahrenheitTemperature = (( 9/5) * celsiusTemperature) + 32
#This line will print the given Celsius Temp in Fahrenheit
print("The Celsius Temperature " + str(celsiusTemperature) + " in Fahrenheit is " + str(fahrenheitTemperature))
