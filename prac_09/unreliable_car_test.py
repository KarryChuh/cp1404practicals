from prac_09.unreliable_car import UnreliableCar

def main():
    unreliable_car = UnreliableCar("Old Car", 100, 50.0)

    for i in range(10):
        distance_driven = unreliable_car.drive(10)
        print(f"Attempt {i+1}: Drove {distance_driven}km. Fuel left: {unreliable_car.fuel} units.")

main()