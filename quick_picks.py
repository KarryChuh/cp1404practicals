import random

NUMBERS_PICK = 6
MIN = 1
MAX = 45

def main():
    number_picks = int(input("How many quick picks? "))

    for _ in range(number_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)

def generate_quick_pick():
    quick_pick = random.sample(range(MIN, MAX + 1), NUMBERS_PICK)
    quick_pick.sort()
    return quick_pick

def print_quick_pick(quick_pick):
    format_quick_pick = " ".join(f"{number:2}" for number in quick_pick)
    print(format_quick_pick)

main()