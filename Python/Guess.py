import random

number = random.randint(1, 100)
guess = 0
attempts = 0

print("🎯 Guess the Number (1 to 100)!")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"🎉 You got it in {attempts} tries!")
