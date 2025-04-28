import string
import random
print("::::::::::::::::::::PASSWORD GENERATOR:::::::::::::::::::::::")
def password_gen(a):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(a))
    return password
while True:
    try:
        num = int(input("Enter the password length:"))
        if num<=0:
            print("Enter a positive number :")
            continue
        password = password_gen(num)
        print("Generated password is ",password)
        
        repeat = input("Do you want to generate another password?(yes/no)").lower()
        if repeat!="yes":
            print("Thank you ...come again")
            break
    except ValueError:
        print("Enter a valid number");
    
