from guitar import Guitar

def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    print(guitar)
    print(f"The {guitar.name} is {guitar.get_age()} years old.")
    print(f"Is the {guitar.name} vintage? {guitar.is_vintage()}")

if __name__ == "__main__":
    main()