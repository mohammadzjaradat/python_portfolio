# login_decision.py
# Check login attempts and credentials in strict order

MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input("Enter username: ")
failed = int(input("Enter failed attempts: "))
password = input("Enter password: ")

if failed >= MAX_FAILED:
    print("Account locked.")
elif username != KNOWN_USER:
    print("Unknown user.")
elif password != STORED_PASSWORD:
    attempts_left = MAX_FAILED - failed - 1
    print(f"Access denied. Attempts left: {attempts_left}")
else:
    print("Access granted.")