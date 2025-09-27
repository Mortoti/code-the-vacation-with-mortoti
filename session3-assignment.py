
# Grading System
score = int(input("Enter your score: "))
if score > 100 or score < 0:
    print("Invalid Score")
elif score >= 90 :
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70 :
    print ("Your grade is C")
elif score >= 60 :
    print("Your grade is D")
else:
    print("Your grade is F")

# Second Assignment

num1 = int(input("Enter the first number: "))
operator = input("Enter the operator(+, -, *, /, %): ")
num2 = int(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1-num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Zero Division Error")
        result = None
        #error if you don't give result a value
    else:
        result = num1/ num2
elif operator == "%":
    if num2 == 0:
        print("Zero Division Error")
        result = None
        #error if you don't give result a value
    else:
        result = num1 % num2
else:
    print("Invalid operator")
    # error if you don't give result a value
if result == None:
    print("Calculation Error. Zero Division Error")
else:
    print(f'{num1} {operator} {num2} = {result}')