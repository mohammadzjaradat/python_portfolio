# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = int(input("New password: "))

# Fix 1: Added missing colon ':' at the end of the if statement
if len(password) < MIN_LENGTH:
    print("- Too short.")

# Fix 2: Changed elif to a separate if statement so both checks run independently
if password == username:
    print("- Same as the username.")

# Fix 3: Reordered conditions so the stricter check (>= 16) comes before (>= 12)
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

# Fix 4: Fixed dictionary-like syntax error in the print statement to use proper f-string format
print(f"Length: {len(password)} ({strength})")