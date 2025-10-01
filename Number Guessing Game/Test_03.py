from contextlib import nullcontext
import random
import time

print("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")
difficulty = input("Enter the number of the prefered difficulty:")
answer_game = 0   # The player's answer.
counter_try = 0   # How many times they tried to guess the number.
counter_game = 1   # How many times they repeated the game.
broke_rule = False   #If they typed a letter in the number guessing game.
is_record = False   #If the new time is a record.
Idontwantto = False

with open("High_Score_Counter_Easy") as reading_easy:
   file_easy = reading_easy.read()
with open("High_Score_Counter_Medium") as reading_medium:
    file_medium = reading_medium.read()
with open("High_Score_Counter_Hard") as reading_hard:
    file_hard = reading_hard.read()

while difficulty != "1" and difficulty != "2" and difficulty != "3":
    try:
        int(difficulty)
    except ValueError:
        print("Only numbers!")
        difficulty = input("Enter the number of the prefered difficulty:")
    else:
        print("Only numbers between 1 and 3!")
        difficulty = input("Enter the number of the prefered difficulty:")

if difficulty == "1":
    print("\nGreat! You have selected the Easiest difficulty level.")
elif difficulty == "2":
    print("\nGreat! You have selected the Medium difficulty level.")
elif difficulty == "3":
    print("\nGreat! You have selected the Hardest difficulty level.")

def hints(num):
    fake_num = num
    print("\nDo you want a hint?")
    hint_answer = input("Yes or No: ")
    while True:
        if hint_answer.lower() == "yes":
            fake_num /= 10
            if int(fake_num) == 0:
                print("This is a single-digit number")
                break
            else:
                print(f"This number starts with {int(fake_num)}.")
                break
        elif hint_answer.lower() == "no":
            print("Oh well...")
            break
        elif hint_answer.lower() != "yes" and "no":
            print("Only 'Yes' or 'No'")
            hint_answer = input("Yes or No: ")

def game():   #For redoing the game.
    global answer_game
    global counter_try
    global counter_game
    global broke_rule
    global difficulty
    global is_record
    global file_easy
    global file_medium
    global file_hard
    start_time = time.time()
    num = int(random.randint(0, 100))
    if counter_game == 1:
        print("Let's start the game!\n")
    else:
        print("Let's start the game again!")
    while int(answer_game) != int(num):
        if difficulty == "1" and counter_try == 10:
            print(f"You Fail! The correct number was {num}.")
            break
        elif difficulty == "2" and counter_try == 5:
            print(f"You Fail! The correct number was {num}.")
            break
        elif difficulty == "3" and counter_try == 3:
            print(f"You Fail! The correct number was {num}.")
            break
        if difficulty == "3" and counter_try == 2:
            hints(num)
        elif difficulty == "2" and counter_try == 4:
            hints(num)
        elif difficulty == "1" and counter_try == 9:
            hints(num)
        answer_game = input("Enter your guess:")
        try:
            int(answer_game)
        except ValueError:
            print("Only numbers!")
            broke_rule = True
            break
        counter_try += 1
        if int(answer_game) != int(num):
            try:
                int(answer_game)
            except ValueError:
                print("Only numbers!")
                broke_rule = True
                break
            if int(num) < int(answer_game):
                print(f"Incorrect! The number is less than {answer_game}.")
            else:
                print(f"Incorrect! The number is greater than {answer_game}.")
    else:
        end_time = time.time()
        elapsed_time = round((end_time - start_time), 3)
        if counter_try == 1:
            print(f"Congratulations! You guessed the correct number in {counter_try} attempt and {elapsed_time} seconds.")
        else:
            print(f"\nCongratulations! You guessed the correct number in {counter_try} attempts and {elapsed_time} seconds.")
        if difficulty == "1" and float(file_easy) > elapsed_time:
            with open("High_Score_Counter_Easy", "w") as placeholder_easy:
                placeholder_easy.write(str(elapsed_time))
            with open("High_Score_Counter_Easy") as reading_easy:
                file_easy = reading_easy.read()
            is_record = True
            print("New Record!")
        elif difficulty == "2" and float(file_medium) > elapsed_time:
            with open("High_Score_Counter_Medium", "w") as placeholder_medium:
                placeholder_medium.write(str(elapsed_time))
            with open("High_Score_Counter_Medium") as reading_medium:
                file_medium = reading_medium.read()
            is_record = True
            print("New Record!")
        elif difficulty == "3" and float(file_hard) > elapsed_time:
            with open("High_Score_Counter_Hard", "w") as placeholder_hard:
                placeholder_hard.write(str(elapsed_time))
            with open("High_Score_Counter_Hard") as reading_hard:
                file_hard = reading_hard.read()
            is_record = True
            print("New Record!")
game()
while counter_game >= 1:
    if broke_rule == False:
        if difficulty == "1" and is_record == False and Idontwantto == False:
            print(f"Your record for Easy difficulty is: {file_easy}")
        elif difficulty == "2" and is_record == False and Idontwantto == False:
            print(f"Your record for Medium difficulty is: {file_medium}")
        elif difficulty == "3" and is_record == False and Idontwantto == False:
            print(f"Your record for Hard difficulty is: {file_hard}")
        print("\nDo you want to play again?")
        answer_repeat = input("Yes or No: ")
        if answer_repeat.lower() == "yes":
            print("\nGreat!\n")
            counter_game += 1
            counter_try = 0
            answer_game = 0
            is_record = False
            game()
        elif answer_repeat.lower() == "no":
            print("Oh well!")
            if counter_game == 1:
                print(f"You have played {counter_game} round.")
            else:
                print(f"You have played {counter_game} rounds.")
            break
        elif answer_repeat.lower() != "yes" and "no":
            print("Only 'Yes' or 'No'")
            Idontwantto = True
    else:
        counter_game = 0
        break

