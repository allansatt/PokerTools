import random

from components.cards import all_hands
from util.preflop_utils import absolute_positions, PreflopRange

correct, total, falsePos, falseNeg = {}, {}, {}, {}
for position in absolute_positions:
    correct[position] = 0
    total[position] = 0
    falsePos[position] = 0
    falseNeg[position] = 0

answer = "y"
preflop_range = PreflopRange()
while answer != "q":
    hand = random.choice(tuple(all_hands()))
    position = random.choice(tuple(absolute_positions))
    action = "open"
    total[position] = total[position] + 1
    answer = input(str(sum(total.values())) + " " + position + " " + action + " " + hand.logical_value)
    if (answer == "y") == (hand in preflop_range[position][action]):
        print("Correct")
        correct[position] = correct[position] + 1
    else:
        if answer == "y":
            falsePos[position] = falsePos[position] + 1
        else:
            falseNeg[position] = falseNeg[position] + 1
        print("Incorrect")

for position in absolute_positions:
    print(position + " open " + str(float(correct[position]) / total[position]) + " correct ")
    print("     " + "False Positives: " + str(falsePos[position]) + "    False Negative: " + str(falseNeg[position]))
print("Total " + float(sum(correct.values())) / sum(total.values()))
