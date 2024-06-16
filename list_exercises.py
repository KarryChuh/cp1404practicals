def main():
    numbers = []
    count = 1
    while True:
        number = float(input(f"Number {count}: "))
        if number < 0:
            break
        numbers.append(number)
        count += 1
    print("\nYou have entered these numbers:")
    for i, number in enumerate(numbers, 1):
        print(f"Number {i}: {number}")
main()