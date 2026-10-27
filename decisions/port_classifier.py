# port_classifier.py
# Classify port numbers and print service name if applicable

port = int(input("Enter port number: "))

if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535.")
else:
    if 0 <= port <= 1023:
        print("Range: system")
    elif 1024 <= port <= 49151:
        print("Range: user")
    else:
        print("Range: dynamic or private")
    
    if port == 22:
        print("Service: ssh")
    elif port == 80:
        print("Service: http")
    elif port == 443:
        print("Service: https")