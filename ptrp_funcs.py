from ptrp_lists import *


"""The first 3 functions ([location]_tribe_questions) will ask the user questions to determine which Polytopia 
tribe is best for them. It prints the tribe message (from end_messages) by accessing the variable storing 
it in the dictionary (in ptrp_lists), then returns the tribe name to add to the list of tribes 
reccomended to user (in ptrp_lists)"""
def eastern_tribe_questions():

    """This function deals solely with the 7 Eastern world Tribes"""

    print('"Eastern!" is incredibly broad so we have to narrow it down a bit')
    east_question = input(
        "Would you (stay) home and build up resources, or (explore) and take from others? ").lower()
    while east_question not in ["stay", "explore"]:
        east_question = input("Invalid option, try again: ").lower()
    if east_question == "stay":
        east_question = input(
            "Do you prefer the company of (elephants), or the taste of fresh (wheat)? Perhaps (fish): ").lower()
        while east_question not in ["elephants", "wheat", "fish"]:
            east_question = input("Invalid option, try again: ").lower()
        if east_question == "fish":
            print(tribe_messages["Kickoo"])
            return "Kickoo"
        elif east_question == "wheat":
            print(tribe_messages["Zebasi"])
            return "Zebasi"
        elif east_question == "elephants":
            print(tribe_messages["Luxidoor"])
            return "Luxidoor"
    else:
        east_question = input("With (sword)s? On (horse)back? Or your bare (hands): ").lower()
        while east_question not in ["hands", "sword", "horse"]:
            east_question = input("Invalid option, try again: ").lower()
        if east_question == "hands":
            print(tribe_messages["Ai-Mo"])
            return "Ai-Mo"
        elif east_question == "sword":
            print(tribe_messages["Xin-Xi"])
            return "Xin-Xi"
        elif east_question == "horse":
            east_question = input("Do you fight best in the (steppe) or the (desert): ").lower()
            while east_question not in ["steppe", "desert"]:
                east_question = input("Invalid option, try again: ").lower()
            if east_question == "steppe":
                print(tribe_messages["Yadakk"])
                return "Yadakk"
            else:
                print(tribe_messages["Oumaji"])
                return "Oumaji"
             
                
def western_tribe_questions():

    """This function deals solely with the 5 Western world Tribes"""

    print("So... 'Western' world... ")
    input("... Are you white? ")
    print("Just kidding, do you like birds? (yes/no)")
    west_question = input("They're nice right: ").lower()
    while west_question not in yes_no_validate:
        west_question = input("Invalid option, try again: ")
    if west_question in yes_list:
        print("Either way, " + tribe_messages["Quetzali"])
        return "Quetzali"
    else:
        print("Oh...")
        west_question = input("Well, castles look nice right (yes/no): ").lower()
        while west_question != "yes" and west_question != "no":
            west_question = input("Invalid option, try again: ")
        if west_question in yes_list:
            west_question = input("You like Old (English) or (Gothic) architecture? ").lower()
            while west_question not in ["english", "gothic"]:
                west_question = input("Invalid option, try again: ").lower()
            if west_question == "english":
                print(tribe_messages["Hoodrick"])
                return "Hoodrick"
            else:
                print(tribe_messages["Vengir"])
                return "Vengir"
        else:
            print("Wow! seriously!?")
            print("You must really hate development and nature in general")
            print("...")
            print("There are TWO tribes that hate nature and development. Like you. But first:")
            west_question = input(
                "Do you prefer the endless, frigid (winter) or so much (heat) you literally just melt away? ").lower()
            while west_question not in ["winter", "heat"]:
                west_question = input("Invalid option, try again: ")
            if west_question == "heat":
                print(tribe_messages["Imperius"])
                return "Imperius"
            else:
                print(tribe_messages["Bardur"])
                return "Bardur"
    
    
def mythical_tribe_questions():
    """This function deals solely with the four Mythical Tribes"""

    print("Wendigo, Dragons, fishmen, and 80 foot centipedes.")
    print("We'll figure out what works for you!")
    myth_question = input("Do you feel comfortable sending your army into the ocean (yes/no): ").lower()
    while myth_question not in yes_no_validate:
        myth_question = input("Invalid option, try again: ").lower()
    if myth_question in yes_list:
        myth_question = input("Okay, but do you actually LIKE fighting in water (yes/no): ").lower()
        while myth_question not in yes_no_validate:
            myth_question = input("Invalid option, try again: ").lower()
        if myth_question in yes_list:
            print(tribe_messages["Aquarion"])
            return "Aquarion"
        else:
            print("Luckily for you, Polaris are super effective against naval units")
            print(tribe_messages["Polaris"])
            return "Polaris"
    else:
        print("You may hate naval combat, but it's gonna bit you in the ass later")
        print("Sorry")
        myth_question = input("Which do you like more? (Dragons) or (Centipedes)? ").lower()
        while myth_question not in ["dragons", "centipedes"]:
            myth_question = input("Invalid option, try again: ").lower()
        if myth_question == "dragons":
            print(tribe_messages["Elyrion"])
            return "Elyrion"
        else:
            print(tribe_messages["Cymanti"])
            return "Cymanti"


"""The next two functions are used only for the payment of tribes should the user say they want to buy some"""

def tribe_payment(total_cost):

    """Shows user all tribes, then allows them to 'buy' a tribe by inputing their name"""

    print("Here are all the tribes:")
    print("---------")
    print("---------")
    print_prices(tribe_prices)
    print("---------")
    print("---------")

    # Purchase loop until user quits

    purchased_tribe = input("Who are we buying? (0 to checkout): ").capitalize()
    while purchased_tribe != "0":
        while purchased_tribe not in all_tribes:
            purchased_tribe = input("Invalid option. Again: ")
        while purchased_tribe in purchased_tribes:
            print("You already bought the", purchased_tribe)
            purchased_tribe = input("Again: ")
        print("You bought the", purchased_tribe + "!")
        # Adds input to list to prevent duplicate inputs
        purchased_tribes.append(purchased_tribe)

        # Adds up price after stashing input

        if purchased_tribe in free_tribes:
            total_cost += 0
        elif purchased_tribe in one_dollar_tribes:
            total_cost += 1
        elif purchased_tribe in two_dollar_tribes:
            total_cost += 2
        else:
            total_cost += 4

        purchased_tribe = input("Buy another tribe? (0 to checkout): ").capitalize()

    # Shows user their cart of purchased tribes, with price of each tribe and total price

    print("---------")
    print("---------")
    print("Your cart")
    print("---------")
    for tribe in purchased_tribes:
        if tribe in free_tribes:
            print(tribe, "($0)")
        elif tribe in one_dollar_tribes:
            print(tribe, "($1)")
        elif tribe in two_dollar_tribes:
            print(tribe, "($2)")
        else:
            print(tribe, "($4)")
    print("Total price: $" + str(total_cost))
    print("Thank you!")


def print_prices(tribe_prices):

    """Prints sheet of all tribes with their prices next to them. If they were recommended to user,
    they are highlighted"""

    for tribe, price in tribe_prices.items():
        if tribe in recommended_tribes:
            print(tribe, price, "(Recommended)")
        else:
            print(tribe, price)


# Not used for purchase function

def suggested_tribe_showcase(recommended_tribes):

    """This last function prints all tribes recommended to user, only used if user doesn't purchase"""

    print("We have suggested", len(recommended_tribes), "tribes for you!")
    for tribe in recommended_tribes:
        print(tribe)