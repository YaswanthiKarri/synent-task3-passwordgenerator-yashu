import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
special_chars = string.punctuation

all_characters = uppercase + lowercase + numbers + special_chars

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:")
print(password)