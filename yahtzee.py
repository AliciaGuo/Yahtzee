import random


def roll(dice, sel):
    if sel is None:
        for i in range(5):
            dice.append(random.randint(1, 6))
    else:
        for i in range(5):
            if sel[i] == 0:
                dice[i] = random.randint(1, 6)


def play():
    s = None
    d = []
    i = 1
    while True:
        roll(d, s)
        if i == 1:
            print("First", end='')
        elif i == 2:
            print("Second", end='')
        else:
            print("Final", end='')
        print(" roll:", *d)
        if i < 3:
            i += 1
            s = [int(x) for x in
                 input("Roll again? [0 to roll, 1 to keep, a single 1 to keep all] ").strip().split(" ")]
            if len(s) == 1:
                break
        else:
            break
    d.sort()
    return d


def three_of_kind(dice):
    counter_list = [0] * 7
    for d in dice:
        counter_list[d] += 1
    for count in counter_list:
        if count >= 3:
            return True
    return False


def four_of_kind(dice):
    counter_list = [0] * 7
    for d in dice:
        counter_list[d] += 1
    for count in counter_list:
        if count >= 4:
            return True
    return False


def yahtzee(dice):
    counter_list = [0] * 7
    for d in dice:
        counter_list[d] += 1
    for count in counter_list:
        if count == 5:
            return True
    return False


def full_house(dice):
    a = None
    b = None
    counter_list = [0] * 7
    for d in dice:
        counter_list[d] += 1
    for count in counter_list:
        if count == 3:
            a = True
        if count == 2:
            b = True
        if a == True and b == True:
            return True
    return False


def contains_small_sequence(dice, sequence):
    seq_index = 0
    for d in dice:
        if d == sequence[seq_index]:
            seq_index += 1
        if seq_index == len(sequence):
            return True
    return False


def is_small_straight(dice):
    return contains_small_sequence(dice, [1, 2, 3, 4]) or contains_small_sequence(dice, [2, 3, 4,
                                                                                         5]) or contains_small_sequence(
        dice, [3, 4, 5, 6])


hello = [1, 1, 2, 5, 4]


def contains_large_sequence(dice, sequence):
    seq_index = 0
    for d in dice:
        if d == sequence[seq_index]:
            seq_index += 1
        if seq_index == len(sequence):
            return True
    return False


def is_large_straight(dice):
    return contains_large_sequence(dice, [1, 2, 3, 4, 5]) or contains_large_sequence(dice, [2, 3, 4, 5, 6])


score = 0
round_number = 0
print("Welcome to Mini Yahtzee!")
while True:
    d = play()

    if full_house(d):
        print("FULL HOUSE!")
        score += 25
    elif yahtzee(d):
        print("YAHTZEE!")
        score += 50
    elif four_of_kind(d):
        print("FOUR OF KIND!")
        score += sum(d)
    elif three_of_kind(d):
        print("THREE OF KIND!")
        score += sum(d)
    elif is_small_straight(d):
        print("SMALL STRAIGHT!")
        score += 30
    elif is_large_straight(d):
        print("LARGE STRAIGHT!")
        score += 40
    else:
        print("CHANCE!")
        score = sum(d)

    round_number += 1
    print("Round:", round_number, "Score:", score)
    n = input("Play again? [q to quit, any other key to continue] ")
    if n.lower() == "q":
        print("Thank you for playing Mini Yahtzee!")
        break
