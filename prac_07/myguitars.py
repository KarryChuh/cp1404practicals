import csv
from guitar import Guitar

FILENAME = "guitars.csv"
def main():
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)
    guitars.sort(key=lambda guitar: guitar.year)
    print("\nGuitars sorted by year:")
    display_guitars(guitars)
    add_new_guitars(guitars)
    save_guitars(FILENAME, guitars)
def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars
def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)
def add_new_guitars(guitars):
    print("\nAdd new guitars:")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
if __name__ == "__main__":
    main()