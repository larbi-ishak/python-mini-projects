import random

choices = ["rock", "paper", "scissors"]

user_choice = input("type your choice\t").strip().lower()

pc_choice = random.choice(choices)

print(user_choice, pc_choice)