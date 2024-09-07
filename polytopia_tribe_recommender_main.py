from ptrp_funcs import *
from ptrp_lists import *

print("Welcome to the Polytopia Tribe Recommendation Program (PTRP)")

# If, for some reason, user wants to skip to purchasing. This allows them to

print("I know this defeats the purpose of it, but...")
user_buying = input("Do you have a tribe in mind? (yes/no): ").lower()
while user_buying not in yes_no_validate:
    user_buying = input("Invalid option, try again: ").lower()
if user_buying in yes_list:
    print("Cool! Let's get straight to payment!")
    purchasing = True
else:
    print("Good. We're gonna have fun!")
    purchasing = False

# Checks if user wants to skip to purchasing first

if purchasing:
    tribe_payment(total_cost)

#####

# Will be set to false when user quits below

looping = True

# Asks user geographical preference to split them off to a specific question set.

while looping:
    print("---------")
    style = input("(Eastern), (Western), or (Mythical) world? ").lower()
    while style not in tribe_category_validate:
        style = input("Invalid option, try again: ").lower()

    # Sets eastern tribe to true, skips the other category functions
    if style in east_validate:
        eastern_tribe = True
        western_tribe = False
        mythical_tribe = False
    # Sets western tribe to true
    elif style in west_validate:
        western_tribe = True
        eastern_tribe = False
        mythical_tribe = False
    else:  # same for mythical
        eastern_tribe = False
        western_tribe = False
        mythical_tribe = True

    print("---------")


    #####

    # Group 1 - Eastern Tribes
    # Xin-Xi, Oumaji, Kickoo, Luxidoor, Zebasi, Ai-Mo, Yadakk
    if eastern_tribe:
        recommended_tribe = eastern_tribe_questions()

    #####

    # Group 2 - Western Tribes
    # Imperius, Bardur, Hoodrick, Vengir, Quetzali
    elif western_tribe:
        recommended_tribe = western_tribe_questions()


    #####

    # Group 3 - Mythical Tribes
    # Polaris, Cymanti, Elyrion, Aquarion
    else:  # mythical_tribe:
        recommended_tribe = mythical_tribe_questions()

    # Adds tribe program suggested to a list for use of purchase function

    if recommended_tribe not in recommended_tribes:
        recommended_tribes.append(recommended_tribe)
    else:
        print("... but we already told you that!")

    print("---------")
    print("---------")
    # Asks user if they want to rerun program
    print("There might be another tribe you like")
    rerun = input("Take the quiz again? (yes/no): ").lower()
    while rerun not in yes_no_validate:
        rerun = input("Invalid option, try again: ").lower()
    if rerun in no_list:
        looping = False

user_buying = input("Would you like to buy any tribe(s)? (yes/no): ")
while user_buying not in yes_no_validate:
    user_buying = input("Invalid option, try again: ").lower()
print("---------")
print("---------")
if user_buying in yes_list:
    tribe_payment(total_cost)
else:
    suggested_tribe_showcase(recommended_tribes)


print("Thanks for using the PTRP!")
