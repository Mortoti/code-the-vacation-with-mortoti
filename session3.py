#------------------SESSION 3 -------------------------------
#IF STATEMENTS
#Comparison
"""
==
!=
<
<=
>
>=
%
"""

"""
if (condition):
    statement
if (it is raining):
    I must go out with an umbrella

"""

# age>= 18 - Adult
# age<18 - Child
age = 2
if age >= 18:
    print("You're an adult")
    #The else does not have a condition
else:
    print("You're a child")

# If
#else if = elif 70 + - Excellent 50+ - Good  <50 - bad
# ASSIGNMENT 
mark = 76
if mark >= 70:
    print("Excellent")
elif mark >= 50:
    print("Good")
else:
    print("Bad")

# else block only runs when the if and the else if block are false
# Even or Odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("Number is odd")
#---------One Student Shared Her To Solve This--------------
# ask the user for a temperature
# temp >= 30 - warm
# temp >= 20 - good
# temp < 20 - cold

# it is not compulsory to always have an else statement

temp = float(input("Enter the temp: "))
if temp >= 30:
    print('warm')
elif temp >= 20:
    print("good")
else:
    print("cold")

