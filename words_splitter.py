# A python module for locating meaningful words inside text.
# probabilistically split concatenated words using NLP based on English Wikipedia unigram frequencies.

import wordninja  # pip install wordninja

flag = True  # Until Loop
while flag:
    print("\n1. Find words from the given string\n2. Exit")
    option = int(input("Enter the Option : "))
    match option:
        case 1:
            user_input = input(
                "Enter the String : "
            )  # gets the user input as string value and stores it in `user_input` variable
            print(f"Founded words : {wordninja.split(user_input)}")
        case 2:
            flag = False
        case _:
            print("Invalid Option\nPlease, Enter a valid option...")
