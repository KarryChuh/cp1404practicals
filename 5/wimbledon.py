import csv
def read_file(filename):
    with open(filename, "r") as in_file:
        reader = csv.reader(in_file)
        data = list(reader)
    return data
def process_champions(data):
    champions = {}
    for row in data:
        name = row[2]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions
def get_countries(data):
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return countries
def display_results(champions, countries):
    print("Wimbledon Champions:")
    for name, wins in champions.items():
        print(f"{name} {wins}")

    sorted_countries = sorted(countries)
    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted_countries))
def main():
    filename = "/Users/zhukerui/PycharmProjects/CP1404Practicals/wimbledon.csv"
    data = read_file(filename)
    champions = process_champions(data)
    countries = get_countries(data)
    display_results(champions, countries)

main()