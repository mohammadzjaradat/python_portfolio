# pin_space_table.py
# Calculate time needed to brute force PINs of length 4 to 8.

GUESSES_PER_SECOND = 10

# Loop over the number of digits from 4 to 8 (range ends at 9 so 8 is included)
for digits in range(4, 9):
    combinations = 10 ** digits
    total_seconds = combinations // GUESSES_PER_SECOND
    
    minutes = total_seconds // 60
    days = minutes // (60 * 24)
    
    print(f"{digits} digits: {combinations} PINs, {minutes} minutes, {days} days")