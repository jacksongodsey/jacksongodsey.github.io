import random

def guess(x):
    random.seed
    random_number = random.randint(1, x)
    print(random_number)
    while True:
        user_guess1= int(input(f"Please enter a random number between 1 and {x}\n"))
        if user_guess1 == random_number:
            print("You guessed correctly")
            break
        elif user_guess1 != random_number:
            print("try again")
  
  
#guess(100)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f"Is {guess} too high (H), too (L), or correct(C)?? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly.")

computer_guess(10)