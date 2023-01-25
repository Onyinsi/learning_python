import random
top_of_range = input("type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("type a number greater than zero")
        quit()
else:
    print("Please type a number next time")
    quit()
RandomNumber = random.randint(0, top_of_range)
score = 0
while True:
    score += 1
    user_guess = input("Please guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number !!")
        continue
    if user_guess == RandomNumber:
        print("you got it right")
        break
    else:
        print("you got it wrong") 
    if user_guess > RandomNumber:
        print("you were above the number") 
    else:
        print("you were below the number") 
print("you guessed it in",score,"guesses")