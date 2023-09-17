import random

secret_number = random.randint(0, 5)
print("let's play number guess game , number will be between 0 and 10")
i = 0
while True:
    try:
        answer = int(input("type your guess\n>"))
        i += 1
        if answer == secret_number:
            print(f"Congrats! you guessed in {i} tries")
            quit()
        else:
            print("wrong!")
    except ValueError:
        print("type a correct number please")

    choice = input(
        "wanna continue or tired from guessing?\ntype q to quit or ENTER to continue")
    if choice.lower() == "q":
        print(f"looser 😠 correct number is :{secret_number}")
        quit()
