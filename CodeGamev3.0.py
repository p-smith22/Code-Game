from colorama import Fore

guess_conversion = {
    1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th",
    11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th", 19: "19th",
    20: "20th", 21: "21st", 22: "22nd", 23: "23rd", 24: "24th", 25: "25th",
}


def initial_code():
    status = 0
    code = 0
    while status == 0:
        try:
            code = list(input("Please input a 4 digit code: "))
            while not len(code) == 4:
                code = list(input("ERROR\nPlease input a 4 digit code: "))
            for digit in code:
                int(digit)
            status = 1
        except ValueError:
            print("ERROR")
            status = 0
    return code


def input_verification(x):
    status = 0
    code = 0
    while status == 0:
        try:
            code = list(input("Please input a 4 digit code(Input \"s\" to skip): "))
            if code[0].lower() == "s":
                if x == 1:
                    print("Other player took first turn")
                    code = 1
                    break
                else:
                    print("Player skipped turn")
                    code = 0
                    break
            else:
                while not len(code) == 4:
                    code = list(input("ERROR\nPlease input a 4 digit code: "))
                for digit in code:
                    int(digit)
                status = 1
        except ValueError:
            print("ERROR")
            status = 0
    return code


def other_code_check(code, x):
    i = 0
    count = 0
    while i < 4:
        if code[i] == your_code[i]:
            count += 1
        i += 1
    if count == 4:
        print(Fore.GREEN + "WINNER! The OTHER player guessed your code in " + str(x) + " guesses!")
        exit()
    else:
        print("Their guess of " + str(code) + " got " + str(count) + " correct.\n")


def guess_count_check(num_correct):

    status = 0
    while status == 0:
        try:
            num_correct = int(num_correct)
            while not num_correct <= 4:
                num_correct = int(input("Please input a number between 0 and 4: "))
            status = 1
        except ValueError:
            print("ERROR")
            num_correct = input("Please input a valid number: ")
    return num_correct


def your_code_check(code, x):
    if code == 0:
        print()
    else:
        guess_correct = input("How many correct did your guess get: ")
        guess_correct = guess_count_check(guess_correct)
        while guess_correct == 4:
            verify = input("Are you sure you got all 4 digits correct? Type \"y\" for YES or \"n\" for NO: ")
            if verify.lower() == "y":
                print(Fore.GREEN + "WINNER! You guessed the code in " + str(x) + " guesses!")
                exit()
            elif verify.lower() == "n":
                guess_correct = input("How many did you actually get correct: ")
                guess_correct = guess_count_check(guess_correct)
            else:
                guess_correct = input("Invalid Input. How many did you actually get correct: ")
                guess_correct = guess_count_check(guess_correct)
        print(Fore.RED + "Your guess " + str(code) + " got " + str(guess_correct) + " correct. \n")


print("First, you will create YOUR password (You will use this for the entirety of the game): ")
your_code = initial_code()
print(Fore.RED + "\nYOUR CODE: " + str(your_code) + "\n")

win = 0
n = 1
s = 1

while win == 0:
    print(Fore.BLUE + "The OTHER player's " + str(guess_conversion.get(n)) + " guess!")
    test1 = input_verification(n)

    if test1 == 1:
        n -= 1
        print()
    elif test1 == 0:
        print()
    else:
        other_code_check(test1, n)

    print(Fore.YELLOW + "YOUR " + str(guess_conversion.get(s)) + " guess!")
    test2 = input_verification(s)
    if test2 == 1:
        s -= 1
        print()
    elif test2 == 0:
        print()
    else:
        your_code_check(test2, s)

    n += 1
    s += 1
