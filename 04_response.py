# lucky unicorn step 2
# generate a random token

# to do
# set up starting amount
# choose 100 tokens
# count # of unicorns and multiply by 5
# count # of horse / zebra and multiply by 0.5
# count # of donkey
# work out total won / lost

import random

HOW_MUCH = 10
tokens = ["horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey", "unicorn"]
unicorn_count = 0
horse_zebra_count = 0
donkey_count = 0

for item in range(0 ,HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count += 1
    elif chosen == "donkey":
        donkey_count += 1
    else:
        horse_zebra_count +=1

    print(chosen)

# Money Calculations...
winnings = unicorn_count * 5 + horse_zebra_count * 0.5

print("**** win / loss calculations*****")
print("# unicorn: {}".format(unicorn_count))
print("# zebra / horse: {}".format(horse_zebra_count))
print("# Donkeys: {}".format(donkey_count))

print()
print("you spent${}".format(HOW_MUCH))
print("You go home with ${:.2f}".format(winnings))





