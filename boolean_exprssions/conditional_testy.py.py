user = "analyst"
role = "viewer"
failed = 3
port = 22

print("Is failed >= 3? I predict True.")
print(failed >= 3)

print("\nIs role == 'admin'? I predict False.")
print(role == 'admin')

print("\nIs port != 80? I predict True.")
print(port != 80)

print("\nIs user == 'analyst' and failed < 5? I predict True.")
print(user == 'analyst' and failed < 5)

print("\nIs not (port == 22)? I predict False.")
print(not (port == 22))

print("\nIs role == 'viewer' or port > 1000? I predict True.")
print(role == 'viewer' or port > 1000)

print("\nIs failed > 5? I predict False.")
print(failed > 5)

print("\nIs user == 'root'? I predict False.")
print(user == 'root')

print("\nIs port <= 80? I predict True.")
print(port <= 80)

print("\nIs not (failed == 3)? I predict False.")
print(not (failed == 3))