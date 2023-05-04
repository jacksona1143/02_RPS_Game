import random


# Functions go here
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # Ask user for choice (and put choice on lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if not in list
        print(error)
        print()


rps_list = ["rock", "paper", "scissors", "xxx"]

while True:
    # comp_choice = random.choice(rps_list[:-1])
    comp_choice = choice_checker("enter comp choice: ", rps_list, "oops")
    user_choice = choice_checker("user choice: ", rps_list, "oops")

    if comp_choice == user_choice:
        result = "tied"

    # three ways to win...
    elif comp_choice == "rock" and user_choice == "paper":
        result = "win"

    # if it's not a tie / win, it's a loss
    else:
        result = "lose"

    print(f"{user_choice} vs {comp_choice}, you {result}")

    # compare choices...
