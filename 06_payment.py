


total = int(input("how much do you want to play with? "))

keep_going = ""
while keep_going == "":

    token = input ("Enter a token: ")

    if token == "unicorn":
        total += 5
        feedback = "congratulations you won $5.00"
    elif token == "donkey":
        total -= 1
        feedback = "sorry you did not win anything this round"
    else:
        total -= 0.5
        feedback = "congratulations you won 50c"

    print()

    print(feedback)
    print("you have {} to play with".format(total))

    if total < 1:
        print("sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("press <enter> to play agian or any key to quit")

print('Thank you for playing.')



