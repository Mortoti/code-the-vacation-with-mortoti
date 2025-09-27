
#-------------------SESSION 4 ------------------------------
# Create an Account
# Login
import getpass
# Creating an account
# username, password

print("=== Welcome To NOLAP Technologies ===")

print("Account Creation")

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
confirm_password = getpass.getpass("Confirm Password: ")

if password == confirm_password:
    print("Account Created Successfully")
    account_created = True
else:
    print("Password Mismatch. Account creation unsuccessful")
    account_created = False

# Login

if account_created:
    print("Hello...This is the Login Page")
    login_username = input("Enter your NOLAP username: ")
    login_password = getpass.getpass("Enter your password: ")
    if login_username == username and login_password == password:
        print(f'Hello {username}. You have been able to Log in Successfully')
    elif login_password != password:
        print("Incorrect Password")
    else:
        print("Username not found")
        
else:
    print("Account not created")
    