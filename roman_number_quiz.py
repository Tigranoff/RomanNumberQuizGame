import time
import random
DEFAULT_NAME = "Player"
INPUT_FILE = "roman_numerals.csv"

def main():
    print_intro()
    name = get_player_name()
    playing = True
    while playing:
        correct = 0
        rounds = get_rounds(name)
        roman_numbers = get_roman_numbers()
        selection = selecting_roman_numbers(rounds, roman_numbers)
        print_countdown()
        print()
        for i in range(1, rounds + 1):
            print(f"ROUND {i}")
            attempts = 3
            while attempts > 0:
                answer = get_player_answer(name, selection[i - 1])
                if not check_answer(answer, roman_numbers, selection[i - 1]):
                    attempts -= 1
                    if attempts > 0:
                        print(f"{name}, try again, you have {attempts} attempt{'s' if attempts > 1 else ''} left")
                    else:
                        print(f"I am Sorry, {name}, the correct answer was {roman_numbers[selection[i-1]]}")

                else:
                    if attempts == 3:
                        correct += 3
                        print("Excellent, you are correct from the first attempt \nYou get 3 points")
                        break
                    elif attempts == 2:
                        correct += 2
                        print("Good, you are correct from the second attempt \nYou get 2 points")
                        break
                    elif attempts == 1:
                        correct += 1
                        print("Congrats, you are correct from the third attempt \nYou get 1 point")
                        break

        print_results(name, correct, rounds)
        playing = get_play_again(name)
    print_outro(name)


def print_intro():
    print("WELCOME TO ROMAN NUMBER QUIZ")
    print("YOU CAN PRACTICE YOUR ROMAN NUMBER SKILLS FROM 1-3999 !!!")
    print('            ---------------------------     ')

def get_player_name():
    name = input("Enter your name: ")
    if name == "":
        print(f"OK, I will call you {DEFAULT_NAME}")
        name = DEFAULT_NAME
    return name

def print_countdown():
    print("GET READY!!!")
    time.sleep(1)
    for i in range(3, 0, -1):
        print(f"{i}...", end="")
        time.sleep(1)

def get_rounds(name):
    rounds = input(f"{name}, Enter the number of rounds you wanna play: ")
    while not(rounds.isdigit() and int(rounds) != 0):
        rounds = input(f"{name}, Enter a number higher than 0: ")
    return int(rounds)

def get_roman_numbers():
    with open(INPUT_FILE) as file:
        roman_numbers = {}
        for line in file:
            if line:
                numerals, rom_numbers = line.split(',')
                roman_numbers[rom_numbers.strip()] = numerals
    return roman_numbers

def selecting_roman_numbers(rounds, roman_numbers):
    selection_of_roman_numbers = []
    roman_numbers_list = list(roman_numbers.keys())
    for i in range(rounds):
        random_roman_number = random.choice(roman_numbers_list)
        while random_roman_number in selection_of_roman_numbers:
            random_roman_number = random.choice(roman_numbers_list)
        selection_of_roman_numbers.append(random_roman_number)
    return selection_of_roman_numbers

def get_player_answer(name, roman_number):
    answer = input(f"{name}, what is the integer value of {roman_number}: \n")
    return answer


def check_answer(answer, roman_numbers, rom_number):
    if answer == roman_numbers[rom_number]:
        return True
    else:
        return False


def get_play_again(name):
    answer = input(f"{name}, Do you want to play again (y or n) \n").lower()
    while not (answer == 'y' or answer == 'n'):
        answer = input(f"{name}, enter y or n \n")
    if answer == 'y':
        return True
    return False

def print_results(name, correct, rounds):
    print(f"{name}, you have scored {correct}/{rounds * 3}")

def print_outro(name):
    print(f"{name}, Thanks for playing")
    input("Press ENTER to exit")

if __name__ == "__main__":
    main()