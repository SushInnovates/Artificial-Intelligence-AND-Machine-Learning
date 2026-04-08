"""
Topic: If-Else Statement Example (Login System)
Day: 12
Description: Simple login verification using nested if-else.
Learning Source: CampusX Python Playlist
"""

# Correct credentials
correct_email = "campusx@gmail.com"
correct_password = "1234"

# User input
email = input("Enter your email: ")

# Check if email contains '@'
if '@' in email:
    
    password = input("Enter your password: ")
    
    if email == correct_email and password == correct_password:
        print("Correct email and password")

    elif email == correct_email and password != correct_password:
        print("Incorrect password")
        
        password = input("Enter your password again: ")
        
        if password == correct_password:
            print("Correct password")
        else:
            print("Incorrect password - Access blocked")

else:
    print("Invalid email format")