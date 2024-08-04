from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    silver_taxi = SilverServiceTaxi("Hummer", 200, 4)

    print(silver_taxi)

    silver_taxi.drive(18)

    print(silver_taxi)
    fare = silver_taxi.get_fare()
    print(f"Fare for 18 km trip: ${fare:.2f}")

    assert abs(fare - 48.78) < 0.01, f"Expected fare: $48.78, but got: ${fare:.2f}"

main()