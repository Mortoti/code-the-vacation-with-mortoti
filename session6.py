"""
QUESTION 1
Mini-Project: Movie Ticket Booking
Scenario:
A user wants to book movie tickets. You’ll simulate the booking system with a small Python program.
Features:
1.	Ask the user’s name.
2.	Let the user choose how many tickets to buy (limit: 5 tickets per person).
3.	Give the user up to 3 attempts if they try to buy more than 5 tickets.
4.	Calculate and print the total cost (assume each ticket costs $12).
5.	Give a friendly message confirming the booking.

attempts = 3
price = 12
name = input("Please enter your name: ")
limit = 5
print(f'Hello, {name}. You are welcome to NOLAP Cinema!')
print("------------------------------------------------\n")
for trials in range(1,4):
    number_of_tickets = int(input("Enter the number of tickets you want to buy.(MAX= 5): "))
    if number_of_tickets > limit:
        print("The total number of tickets an individual can buy is 5.")
        print(f'You are left with {attempts-trials} attempt(s)')
        continue
    elif number_of_tickets < 1:
        print("Invalid number")
        print(f'You are left with {attempts-trials} attempt(s)')
        continue
    else:
        print("You have successfully purchased your ticket(s) from NOLAP Cinema")
        print("-------------RECEIPT-------------------")
        print(f'Name: {name}\n')
        print(f'Number of Tickets Purchased: {number_of_tickets}\n')
        print(f"Price Per Ticket: {price} dollars\n")
        print(f'Total Price: {price * number_of_tickets} dollars')
        break
else:
    print("After three attempts..You still failed to purchase your ticket")

"""







"""
QUESTION 2
Mini-Project: Quiz Game
Scenario:
You’re creating a small Python quiz game to test general knowledge. The user will answer multiple-choice questions, and the program will give immediate feedback at the end based on their score.
Features:
1.	Ask for the user’s name.
2.	Present 3 multiple-choice questions (hard-coded).
3.	Keep track of correct answers.
4.	Print the total score and personalized feedback at the end.
"""

score = 0
marks = 30

name = input("Enter your name: ")
print(f'Hello, {name}. You are welcome to Uni Quiz')
print("------------------------------------------\n")

print("---------QUESTION 1-----------------\n")
print("What is the best University in Ghana currently? \n")
print("A. Legon")
print("B. UHAS")
print("C. UCC")
print("D. KNUST\n")
option = input(">>> ")
answer = "D"
if answer == option.upper():
    print("You nailed it !")
    score += marks
else:
    print("My bad !")
    print(f'The correct answer is {answer}')
print("\n\n")
print("------------------QUESTION 2---------------------\n")
print("What is the easiest programming language in the world? \n")
print("A. Python")
print("B. Kotlin")
print("C. C#")
print("D. Dart\n")
option = input(">>> ")
answer = "A"
# I used the upper to convert the user's input to match the case of my answer
if answer == option.upper():
    print("You nailed it !")
    score += marks
else:
    print("My bad !")
    print(f'The correct answer is {answer}')
print("\n\n")

print("--------------------QUESTION 3 ----------------\n")
print("Which of the following is a framework for Python? \n")
print("A. Flutter")
print("B. Django")
print("C. .NET")
print("D. Spring Boot\n")
option = input(">>> ")
answer = "B"

if answer == option.upper():
    print("You nailed it !")
    score += marks
else:
    print("My bad !")
    print(f'The correct answer is {answer}')

total_score = (score/90)* 100

print("\n")

if total_score >= 70:
    remarks = "Excellect"
elif total_score >=50:
    remarks = "Good"
else:
    remarks = "Bad"
print("-----------------------REPORT CARD -------------\n")

print(f"Name: {name}")
print(f'Total Score: {round(total_score, 2)}%')
print(f'Remark: {remarks}')

    












"""
QUESTION 3
Mini-Project: ATM Deposit/Withdrawal Simulation
Scenario:
Simulate a small ATM system where the user can deposit or withdraw money, and the balance updates after each transaction. The user gets 3 transactions.
Features:
1.	Start the user with a balance of 1000.
2.	Ask the user 3 times whether they want to deposit or withdraw.
3.	Update and display the balance after each operation.
4.	Handle invalid inputs (e.g., withdrawing more than the balance, non-numeric input).
"""
 