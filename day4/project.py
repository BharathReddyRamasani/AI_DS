from abc import ABC, abstractmethod
import time
class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate
        self.__owner_name = owner_name
    def get_license_plate(self):
        return self.__license_plate
    def get_owner_name(self):
        return self.__owner_name
    def display(self):
        print(f"License Plate: {self.__license_plate}, Owner: {self.__owner_name}")
    def cal_parking(self, hours):
        return 0
class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet=True):
        super().__init__(license_plate, owner_name)
        self.helmet = helmet
    def display(self):
        print(f"License Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet: {self.helmet}")
    def cal_parking(self, hours):
        return 20 * hours
class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats
    def display(self):
        print(f"License Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}")
    def cal_parking(self, hours):
        return 50 * hours
class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel = four_wheel

    def display(self):
        print(f"License Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Four-Wheel: {self.four_wheel}")

    def cal_parking(self, hours):
        return 70 * hours
class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, load_cap=10000):
        super().__init__(license_plate, owner_name)
        self.load_cap = load_cap

    def display(self):
        print(f"License Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Load Cap: {self.load_cap}")

    def cal_parking(self, hours):
        return 100 * hours
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size
        self.__is_occupied = False
        self.__vehicle = None
        self.__start_time = None

    def is_available(self):
        return not self.__is_occupied

    def assign_vehicle(self, vehicle):
        if self.is_available() and self._fits(vehicle):
            self.__vehicle = vehicle
            self.__is_occupied = True
            self.__start_time = time.time()
            print(f"Vehicle {vehicle.get_license_plate()} parked at Spot {self.spot_id}")
            return True
        return False

    def remove_vehicle(self):
        if self.__is_occupied:
            end_time = time.time()
            hours = max(1, int((end_time - self.__start_time) // 3600) + 1)
            fee = self.__vehicle.cal_parking(hours)
            vehicle = self.__vehicle
            self.__vehicle = None
            self.__is_occupied = False
            self.__start_time = None
            return vehicle, fee
        return None, 0

    def _fits(self, vehicle):
        if isinstance(vehicle, Bike) and self.size in ["S", "M", "L", "XL"]:
            return True
        if isinstance(vehicle, Car) and self.size in ["M", "L", "XL"]:
            return True
        if isinstance(vehicle, SUV) and self.size in ["L", "XL"]:
            return True
        if isinstance(vehicle, Truck) and self.size == "XL":
            return True
        return False

    def __str__(self):
        status = "Occupied" if self.__is_occupied else "Available"
        return f"Spot {self.spot_id} ({self.size}) - {status}"
class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            print(spot)

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.assign_vehicle(vehicle):
                return True
        print(f"No suitable spot available for {vehicle.get_license_plate()}")
        return False

    def unpark_vehicle(self, vehicle):
        for spot in self.spots:
            v, fee = spot.remove_vehicle()
            if v and v.get_license_plate() == vehicle.get_license_plate():
                print(f"Vehicle {v.get_license_plate()} unparked. Fee: ₹{fee}")
                return fee
        print(f"Vehicle {vehicle.get_license_plate()} not found.")
        return 0
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Cash.")
class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Card.")
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI.")
