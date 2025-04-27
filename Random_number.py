import random 

num = random.randrange(1,100)
life = 5
guess = 0
print("Welcome to the Number guessing game !\nYou have 5 chances to guess the number between 1 to 100")
while guess < life:
    guess = guess + 1
    g_num  = int(input("Enter your guess: "))
    if g_num == num:
        print("Congratulations! You have guessed the number")
        break
    elif guess == life:
        print("You have run out of chances :(, The number was: ", num)
        break               
    elif g_num < num:
        print("You guessed too low")
    elif g_num > num:
        print("You guessed too high")
