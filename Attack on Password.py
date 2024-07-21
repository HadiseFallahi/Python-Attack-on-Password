import random
password = int(input("enter the password:"))
guess = 0
while guess != password:
    guess = random.randint(100000, 999999)
    print(guess)
print("The password is " + str(guess))
