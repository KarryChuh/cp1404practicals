from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Display the available taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Prompt the user to choose a taxi from the list."""
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None

def drive_taxi(taxi, bill):
    """Prompt the user to drive the selected taxi and update the bill."""
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return bill

    try:
        distance = float(input("Drive how far? "))
        fare = taxi.get_fare()
        taxi.drive(distance)
        fare = taxi.get_fare() - fare  # Update fare after driving
        bill += fare
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        print(f"Bill to date: ${bill:.2f}")
    except ValueError:
        print("Invalid input")

    return bill

def main():
    """Main function to run the taxi simulator."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    while True:
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").strip().lower()
        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")

main()