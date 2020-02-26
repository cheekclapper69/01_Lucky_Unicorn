# lucky unicorn step 1
# get initial amount and check that its valid

# integer checking function

def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "whoops! please enter an integer between {} and {}".format(low, high)

        try:
            response = int(input("Enter an integer between {} and {}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

    print(response)

# main routine

how_much = intcheck("How much money do you want to play with? ", 1, 10)






