# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:36:00 2020

@author: mokarram
"""
import sys
import time
import random



def print_pause(message):
    print(message)
    time.sleep(1.8)

def intro():
    print_pause("You find yourself in a samll village " 
                 "evening time")
    print_pause("Dangerous outside")
    print_pause("Reach home on the opposite side of "
                "village")

    
def valid_input(message, options):
    while True:
        response = input(message).lower()
        for option in options:
            if option in response:
                response = option
                return response
        print_pause("Sorry, Not list")

        

def trick_or_treaters(item, play_again_list):
    if item == "Angry birds":
        print_pause("Angry Birds made trick-or-treaters very happy.")
        print_pause(" Next ")
    else:
        if item == "guns":
            print_pause("Your guns scared the trick-or-treaters and "
                        "made them cry.")
        elif item == "holy water":
            print_pause("Holy water isn't something trick-or-treaters expect "
                        "to get at Halloween!. It only made them cry.")
        print_pause("Their angry parents kicked you out of the village.")
        print_pause("You lost! You didn't manage to reach your home.")
        play_again(play_again_list)


def zombies(item, play_again_list):
    if item == "guns":
        print_pause("With your guns you shot directly to zombies' heads.")
        print_pause("All zombies died! You may continue your way.")
    elif item == "candies" or item == "holy water":
        print_pause("This wasn't effektive against zombies!")
        print_pause("You lost! You've also become a zombie and "
                    "you won't come back home.")
        play_again(play_again_list)


def vampires(item, play_again_list):
    if item == "holy water":
        print_pause("You splashed the vampires with holy water.")
        print_pause("All vampires died! You may continue your way.")
    elif item == "candies" or item == "guns":
        print_pause("This wasn't effektive against vampires!")
        print_pause("You lost! You've also become a vampire and "
                    "you won't come back home.")
        play_again(play_again_list)


def action_1(enemy, item, items_trunk, play_again_list, enemies):
     
    enemies.remove(enemy)
    if enemy == "trick-or-treaters":
        trick_or_treaters(item, play_again_list)
    elif enemy == "zombies":
        zombies(item, play_again_list)
    elif enemy == "vampires":
        vampires(item, play_again_list)
    print_pause("Your bag is empty again.")
    items_trunk.append(item)

    
def action_2(enemy, item, items_trunk, play_again_list, enemies):
    print_pause("You are back at the old trunk.")
    print_pause(f"Which item do you want to exchange {item} for?\n")
    items_trunk.append(item)
    print_pause(f" - {items_trunk[0].capitalize()}\n"
                f" - {items_trunk[1].capitalize()}\n")
    item = valid_input("Please, enter a name of the item.\n", items_trunk)
    print_pause(f"You put {item} in your bag and return to the {enemy}.")
    items_trunk.remove(item)
    action_1(enemy, item, items_trunk, play_again_list, enemies)

    
def find_trunk(items_trunk):
    print_pause("Further on your way, you find an old trunk with "
                "three items in it.")
    print_pause("However, only one item can suit into your bag.")
    print_pause("Which item would you like to take?\n")
    print_pause(f" - {items_trunk[0].capitalize()}\n"
                f" - {items_trunk[1].capitalize()}\n"
                f" - {items_trunk[2].capitalize()}\n")
    item = valid_input("Please, enter a name of the item.\n", items_trunk)
    print_pause(f"You put {item} in your bag and continue your way.")
    items_trunk.remove(item)
    return item


def meet_enemy(item, items_trunk, actions, play_again_list, enemies):
     
    enemy = random.choice(enemies)
    print_pause(f"Suddenly, you've been approached by a bunch of {enemy}.")
    print_pause("What's your next step?\n")
    print_pause(f" 1. Get your {item} out of the bag.\n"
                " 2. Run back to the old trunk to exchange your item.\n")
    action = valid_input("Please enter a number 0 or 1.\n", actions)
    if action == '0':
        action_1(enemy, item, items_trunk, play_again_list, enemies)
    elif action == '1':
        action_2(enemy, item, items_trunk, play_again_list, enemies)


def play_again(play_again_list):
    print_pause("Would you like to play again?")
    response = valid_input("Please, enter yes or no.\n", play_again_list)
    if response == "yes":
        print_pause("Great! Restarting the game...\n")
        play_game()
    elif response == "no":
        sys.exit()


def game_body(items_trunk, enemies, actions, play_again_list):
    while len(enemies) != 0:
        item = find_trunk(items_trunk)
        meet_enemy(item, items_trunk, actions, play_again_list, enemies)
    print_pause("Congratulatons!")
    print_pause("You defeated all enemies and safely reached your home!")
    play_again(play_again_list)


def play_game():
    items_trunk = ["Angry birds", "guns", "holy water"]
    enemies = ["trick-or-treaters", "zombies", "vampires"]
    actions = ['0', '1']
    play_again_list = ["yes", "no"]
    intro()
    game_body(items_trunk, enemies, actions, play_again_list)


play_game()