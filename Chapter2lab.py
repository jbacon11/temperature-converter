#Celsius to Fahrenheit temperature converter
#Jeremy Bargy
#Jan. 8, 2020

#Initalize variables

userName = "" #str
temperature= 0.0 #float / celsius
fahTemp= 0.0 #float

#user data name and celsius temperature
userName= input('Please enter your name: \n')
temperature= float(input('Please enter your Celsius temperature: \n'))

#Calculations
fahTemp= (9/5)*temperature + 32

#Display results to user
print(userName, '\'s Fahrenheit Temperature:\t', fahTemp)
