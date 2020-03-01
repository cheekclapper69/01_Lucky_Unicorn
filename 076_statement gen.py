# fully working program
# needs testing

import random

name = input("What is your name? ")
print("---------------------------")
print("Hello", name)
print("--------------")

def intcheck(question, low, high):
    valid = False
    error = "Please enter an number between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)


def token_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# main

COST = 1
UNICORN = 5
HORSE_ZEBRA = 0.5
DONKEY = 0

print("**** Welcome to lucky Unicorn game ****")
print()
print("To play, enter an amount of money between 41 and $10 (whole dollars only),")
print()
print("- it costs $1/round")
print()
print("Payouts...")
print("-Unicorn: ${:.2f}".format(UNICORN))
print("-HORSE / ZEBRA:${:.2f}".format(HORSE_ZEBRA))
print("-DONKEY: ${:.2f}".format(DONKEY))
print()

balance = intcheck("How much money would you like to play with?", 1 , 10)
round_count = 0

print("***** Game in progress ******")

keep_going = ""
while keep_going =="":

    # tokens list
    tokens = ["Horse", "Horse" "Horse",
              "Zebra", "Zebra", "Zebra",
              "Donkey", "Donkey", "Donkey", "Unicorn"]

    # randomly chosen token
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))


    # adjust the based balance
    if token == "Unicorn":
        token_statement("***** Congratulations! it's a ${:.2f} {}*****".format(UNICORN, token), "*")
        balance += UNICORN


    elif token == "Donkey":
        token_statement("-- Sorry. it's a {}.  You did not win anything this round --".format(token), "-")
        balance -= COST

    else:
        token_statement("^^ Good try. it's a {}.  You won back 50c ^^".format(token), "^")
        balance -= HORSE_ZEBRA

    print()
    print("Rounds played: {}        Balance: ${:.2f}".format(round_count, balance))
    print()

    # if user has enough money left to play ash if they want to play again...
    if balance < COST:
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play agian or any key to quit")
    print("---------------------------------------------------")
    # farewell to user
    print('Thank you for playing.', name)
    print("---------------------------")










