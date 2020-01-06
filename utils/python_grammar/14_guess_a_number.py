from random import randint

secret_number = randint(1,100)

guess = int(input("Guess the secret number: "))
while guess != secret_number:
    if guess < secret_number:
        print("My secret number is bigger")
    else:
        print("My secret number is smaller")
    guess = int(input("Guess the secret number again: "))

print("Congrats!")
