# Lab 11.27
"""This program will store roster and rating information for a soccer team.
    Coaches rate players during tryouts to ensure a balanced team."""

# key: jersey number (0 - 99)
# value: player rating (1 - 9)
player_dict = {}
sorted_list_keys = []  # sorted list to store the jersey numbers


# function to sort dictionary keys
def sort_dict_keys():
    # sort the dictionary keys and then store them into
    # a list, then return that list
    sorted_list_keys = sorted(player_dict.keys())
    return sorted_list_keys


# OBJ 3:
# Define the function output_roster().
def output_roster():

    # Call the sort_dict_keys() function to get
    # sorted list of dictionary keys.
    sorted_list_keys = sort_dict_keys()
    print('ROSTER')

    # For loop to run through the list of keys
    for i in sorted_list_keys:

        # Display jersey number and player's rating
        # sorted by jersey number.
        print("Jersey number: {}, Rating: {}".format(i, player_dict[i]))


# OBJ 4:
# Define add_player() function.
def add_player():
    # Prompt user to enter a jersey number
    print("Enter a new player's jersey number:")
    jersey_num = int(input())

    # Check if jersey number is between 0 - 99.
    # If not, ask user to enter a jersey number again.
    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please enter again!")
        print("Enter a new player's jersey number:")
        jersey_num = int(input())

    # Prompt user to enter player's rating.
    print("Enter the player's rating:")
    player_rating = int(input())

    # Check if player_rating is between 1 - 9
    # If not, ask user to enter player_rating again.
    while (player_rating < 1) or (player_rating > 9):
        print("Invalid Rating! Please enter again!")
        print("Enter the player's rating:")
        player_rating = int(input())

    # Update the player dictionary (player_dict) with
    # the new entry.
    player_dict.update({jersey_num : player_rating})


# OBJ 5:
# Define delete_player() function
def delete_player():

    # Prompt user for a player's jersey number.
    print("Enter a jersey number:")
    jersey_number = int(input())

    # Remove that player from the roster (delete jersey number and rating)
    if jersey_number in player_dict:
        del player_dict[jersey_number]


# OBJ 6:
# Define update_player_rating() function
def update_player_rating():

    # Prompt user for player's jersey number
    print("Enter a jersey number:")
    jersey_number = int(input())

    # Check if jersey number is between 0 - 99
    # If not prompt user again to enter jersey number
    while (jersey_number < 0) or (jersey_number > 99):
        print("Invalid jersey number! Please enter again!")
        print("Enter a jersey number:")
        jersey_number = int(input())

    # Prompt user for the player's new rating
    print("Enter a new rating for player:")
    player_rating = int(input())

    # Make sure player rating is between 1 - 9
    while (player_rating < 1) or (player_rating > 9):
        print("Invalid rating! Please enter again!")
        print("Enter a new rating for player:")
        player_rating = int(input())

    # Update player's rating by updating
    # the key, value pair in player_dict
    player_dict[jersey_number] = player_rating

# Define output_player_above_rating() function
def output_player_above_rating():

    # Prompt user for a rating.
    print("Enter a rating:")
    rating = int(input())

    # Make sure rating is between 1 - 9
    while (rating < 1) or (rating > 9):
        print("Invalid rating! Please enter again!")
        print("Enter a rating:")
        rating = int(input())

    # Print specified rating
    print("ABOVE {}".format(rating))

    # Call sort_dict_keys() function to get sorted list
    #  of keys from player_dict
    sorted_list_keys = sort_dict_keys()

    # Search the list of keys
    for i in sorted_list_keys:
        # If current rating in the dictionary is
        # greater than the entered rating then...
        if player_dict[i] > rating:
            # Print the current player's jersey number
            # and rating
            print("Jersey number: {}, Rating: {}".format(i, player_dict[i]))


# OBJ 1:
# Prompt user to input five pairs of numbers,
# a player's jersey number (0 - 99) and the player's rating (1 - 9).
# Store the jersey numbers and ratings in a dictionary then
# output the dictionary's elements w/ the jersey numbers in ascending order

# Begin a For loop from 1 to 6
for i in range(1, 6):

    # Prompt user to enter player's jersey number.
    print("Enter player {}'s jersey number:".format(i))
    jersey_number = int(input())

    # Make sure jersey_number is between 0 - 99
    while (jersey_number < 0) or (jersey_number > 99):
        print("Invalid jersey number! Please enter again!")
        print("Enter player {}'s jersey number:".format(i))
        jersey_number = int(input())

    # Prompt user to enter a player's rating
    print("Enter player {}'s rating:".format(i))
    player_rating = int(input())

    # Make sure player rating is within 1 - 9
    while (player_rating < 1) or (player_rating > 9):
        print("Invalid rating! Please enter again!")
        print("Enter player {}'s rating:".format(i))
        player_rating = int(input())

    print()

    # Add jersey number as value and
    # player rating as key in player_dict dictionary.
    player_dict[jersey_number] = player_rating

    # Call the output_roster() function to display
    # player's details.
output_roster()
print()

# OBJ 2:
# Add a menu of options. Each option is represented by a single character.
# The program will initially output the menu, then menu is outputted again
# after user chooses an option. Program ends when user chooses the option
# to Quit.

# Start a While Loop:
while True:

    # Display the menu.
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()

    # Prompt user to choose an option.
    print("Choose an option:")
    user_choice = input()

    # If option (a) is chosen, call add_player() function.
    if user_choice == 'a':
        add_player()

    # If option (d) is chosen, call delete_player() function.
    elif user_choice == 'd':
        delete_player()

    # If option (u) is chosen, call update_player_rating() function.
    elif user_choice == 'u':
        update_player_rating()

    # If option (r) is chosen, call output_player_above_rating() function.
    elif user_choice == 'r':
        output_player_above_rating()

    # If option (o) is chosen, call output_roster() function.
    elif user_choice == 'o':
        output_roster()

    # If option (q) is chosen, break the While Loop.
    elif user_choice == 'q':
        break
    print()
