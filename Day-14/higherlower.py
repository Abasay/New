from art import logo
from art import vs
from game_data import data
import random
from os import system

def print_logo(words, scores):
    print()
    print(logo)
    if scores >= 0:
        print(words)
    print()

def print_vs():
    print()
    print(vs)
    print()

first_random = random.choice(data)
second_random = random.choice(data)
score = 0
word = ""

def compare(first, second, score_count, word):
    print_logo(word, score_count)
    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}.")
    print_vs()
    print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}.")
    followers = input("Who has more followers? Type 'A' or 'B': ").lower()

    if (first['follower_count'] > second['follower_count']) and followers == 'a':
        
        system('cls')
        score_count += 1
        word = f"You're right! Current score: {score_count}"
        first =  second
        second = random.choice(data)
        
        compare(first, second, score_count, word)
    elif (first['follower_count'] < second['follower_count']) and followers == 'b':
        
        system('cls')
        word = f"You're right! Current score: {score_count}"
        score_count += 1
        first =  second
        second = random.choice(data)
        
        compare(first, second, score_count, word)
    elif (first['follower_count'] == second['follower_count']):
      
        system('cls')
        word = f"That is a draw. Current score: {score_count}"
        score_count += 0
        first =  second
        second = random.choice(data)
        
        compare(first, second, score_count, word)
    else:
        system('cls')
        score_count += 0
        word = f"You're wrong: final score is {score_count}"
        print_logo(word, score_count)

compare(first_random, second_random, score, word)