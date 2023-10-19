import random


chars = "abcdefghijklmnopqrstuvwxyz123456789!#$%&/(=+-{*?¿¡}][{"

print("GENERATOR OF PASSWORDS")

while True:

    password = ""

    for i in range(16):
        password += random.choice(chars)

    print(f"Your Password: {password}")

    user_input = input("¿You Want To Generate A New Password?: ").strip().lower()

    if user_input != "yes":
        break    

