from art import logo, vs
from game_data import data
import random


def game_start(current_score, first_person):
    print(logo)
    if current_score > 0:
        print(f"You're right!. Current Score: {current_score}")
    # First Celebrity
    print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}.")

    print(vs)
    # Second Celebrity
    second_person = random.choice(data)
    if first_person == second_person:
        second_person = random.choice(data)
    print(f"Against B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}.")

    choice = input("Who has more followers? Type 'A' or 'B': ")
    game_continue = True

    while game_continue:
        if first_person['follower_count'] > second_person['follower_count'] and choice.lower() == 'a':
            current_score += 1
            game_start(current_score, first_person)
        elif first_person['follower_count'] < second_person['follower_count'] and choice.lower() == 'b':
            current_score += 1
            first_person = second_person
            game_start(current_score, first_person)
        else:
            print(f"Sorry, that's wrong. Final Score: {current_score}")
            game_continue = False
        break


game_start(current_score=0, first_person=random.choice(data))
