from end_messages import *

######################################################################

# Tribes put in lists by cost, for purchasing function
# Input validation + Price validation

free_tribes = ["Xin-xi", "Imperius", "Bardur", "Oumaji"]

one_dollar_tribes = ["Kickoo", "Hoodrick", "Vengir", "Zebasi", "Ai-mo", "Quetzali", "Yaddak"]

two_dollar_tribes = ["Aquarion", "Elyrion", "Polaris", "Cymanti"]

four_dollar_tribes = ["Luxidoor"]

all_tribes = free_tribes + one_dollar_tribes + two_dollar_tribes + four_dollar_tribes

# Empty list to print all tribes user bought for purchasing function
purchased_tribes = []

# Empty list for all tribes reccomended to user,
# will be highlighted in purchase screen if user decides to purchase tribes
recommended_tribes = []

# Counter variable for total price
total_cost = 0

# End of program messages,
# Strings are defined in end_messages file for readability

tribe_messages = {"Xin-Xi": xin_xi_msg,
                  "Imperius": imperius_msg,
                  "Bardur": bardur_msg,
                  "Oumaji": oumaji_msg,
                  "Luxidoor": luxidoor_msg,
                  "Kickoo": kickoo_msg,
                  "Hoodrick": hoodrick_msg,
                  "Vengir": vengir_msg,
                  "Zebasi": zebasi_msg,
                  "Ai-Mo": ai_mo_msg,
                  "Quetzali": quetzali_msg,
                  "Yadakk": yadakk_msg,
                  "Aquarion": aquarion_msg,
                  "Elyrion": elyrion_msg,
                  "Polaris": polaris_msg,
                  "Cymanti": cymanti_msg}

# Displays prices of all tribes to user

tribe_prices = {"Xin-Xi": "(Free)",
                "Imperius": "(Free)",
                "Bardur": "(Free)",
                "Oumaji": "(Free)",
                "Luxidoor": "($4.00)",
                "Kickoo": "($1.00)",
                "Hoodrick": "($1.00)",
                "Vengir": "($1.00)",
                "Zebasi": "($1.00)",
                "Ai-Mo": "($1.00)",
                "Quetzali": "($1.00)",
                "Yaddak": "($1.00)",
                "Aquarion": "($2.00)",
                "Elyrion": "($2.00)",
                "Polaris": "($2.00)",
                "Cymanti": "($2.00)"}

# Input validation lists

yes_list = ("yes", "yeah", "y")

no_list = ("no", "nah", "n")

yes_no_validate = yes_list + no_list

east_validate = ("eastern", "east")

west_validate = ("western", "west")

myth_validate = ("mythical", "myth")

tribe_category_validate = east_validate + west_validate + myth_validate
