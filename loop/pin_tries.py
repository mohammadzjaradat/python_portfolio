# pin_tries.py
# Check a PIN with three tries.

MAX_TRIES = 3
CORRECT_PIN = "2580"

tries = 0
access_granted = False

while tries < MAX_TRIES:
    pin = input("PIN: ")
    tries += 1

    if pin == CORRECT_PIN:
        print("Access granted.")
        access_granted = True
        break
    else:
        print(f"Wrong PIN. Tries left: {MAX_TRIES - tries}")

if not access_granted:
    print("Card blocked.")