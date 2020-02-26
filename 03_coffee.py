
    if token == "unicorn":
        # prints unicorn statement
        print()
        print("***********************************************************")
        print("*****    Congratulations! it,s a ${:.2f} {}*****".format(UNICORN, token))
        print("***********************************************************")

        balance += UNICORN      # wins $5

    elif token == "donkey":

        print()
        print("---------------------------------------------------------------")
        print("| Sorry. it's a {}. You did not win anything this round |".format(token))
        print("---------------------------------------------------------------")

        balance -= COST  # wins nothing (loses $1)

    else:

        print()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("< Good try. It's a {}. You won back 50c>".format(token))
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        balance -= horse_zebra  # 'wins' 50c, paid $1 so loses 50c