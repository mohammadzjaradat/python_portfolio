# Fix 1: runtime error
def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


print_header()


# Fix 2: semantic error
def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        total = failed * minutes
        return total
    return 0


# Fix 3: indentation error
def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


# Fix 4: wrong keyword argument
print(login_line(username="sara", failed=4))
print(login_line("omar", 1))