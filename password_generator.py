import random
import string

def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

# Test output
print("Generated Password:", make_password(10))
