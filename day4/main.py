from project import Bike, Car, SUV, Truck, ParkingSpot, ParkingLot, CashPayment, CardPayment, UPIPayment
def choose_payment_method():
    print("\nSelect Payment Method:")
    print("1. Cash")
    print("2. Card")
    print("3. UPI")
    choice = input("Enter choice: ")
    if choice == "1":
        return CashPayment()
    elif choice == "2":
        return CardPayment()
    elif choice == "3":
        return UPIPayment()
    else:
        print("Invalid choice, defaulting to Cash.")
        return CashPayment()
if __name__ == "__main__":
    lot = ParkingLot()
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "L"))
    lot.add_spot(ParkingSpot(4, "XL"))
    vehicles = []
    while True:
        print("\n===== Parking System =====")
        print("1. Add Vehicle & Park")
        print("2. Show Parking Spots")
        print("3. Unpark Vehicle")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            vtype = input("Enter vehicle type (bike/car/suv/truck): ").lower()
            plate = input("Enter license plate: ")
            owner = input("Enter owner name: ")
            if vtype == "bike":
                v = Bike(plate, owner)
            elif vtype == "car":
                v = Car(plate, owner)
            elif vtype == "suv":
                v = SUV(plate, owner)
            elif vtype == "truck":
                v = Truck(plate, owner)
            else:
                print("Invalid vehicle type!")
                continue
            vehicles.append(v)
            parked = lot.park_vehicle(v)
            if parked:
                print(f"{vtype.capitalize()} {plate} parked successfully!")
        elif choice == "2":
            lot.show_spots()
        elif choice == "3":
            plate = input("Enter license plate to unpark: ")
            vehicle = None
            for v in vehicles:
                if v.get_license_plate() == plate:
                    vehicle = v
                    break

            if not vehicle:
                print("Vehicle not found!")
                continue

            fee = lot.unpark_vehicle(vehicle)
            if fee > 0:
                payment = choose_payment_method()
                payment.process_payment(fee)

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")
