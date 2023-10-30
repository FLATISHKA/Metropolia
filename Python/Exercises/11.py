from main import function_driver
import random


class Exc:
    class Publication:
        def __init__(self, name):
            self.name = name

        def print_information(self):
            raise NotImplementedError("Subclasses should implement this method.")

    class Book(Publication):
        def __init__(self, name, author, page_count):
            super().__init__(name)
            self.author = author
            self.page_count = page_count

        def print_information(self):
            print(f"Book Name: {self.name}")
            print(f"Author: {self.author}")
            print(f"Page Count: {self.page_count}")

    class Magazine(Publication):
        def __init__(self, name, chief_editor):
            super().__init__(name)
            self.chief_editor = chief_editor

        def print_information(self):
            print(f"Magazine Name: {self.name}")
            print(f"Chief Editor: {self.chief_editor}")

    class Car:
        def __init__(self, registration_number, maximum_speed):
            self.registration_number = registration_number
            self.maximum_speed = maximum_speed
            self.current_speed = 0
            self.travelled_distance = 0

        def drive(self, hours):
            speed_change = random.randint(-10, 15)
            new_speed = self.current_speed + speed_change
            self.current_speed = max(0, min(new_speed, self.maximum_speed))
            distance = self.current_speed * hours
            self.travelled_distance += distance

        def __str__(self):
            return f"{self.registration_number}: {self.travelled_distance} km travelled."

    class ElectricCar(Car):
        def __init__(self, registration_number, maximum_speed, battery_capacity_kWh):
            super().__init__(registration_number, maximum_speed)
            self.battery_capacity_kWh = battery_capacity_kWh

    class GasolineCar(Car):
        def __init__(self, registration_number, maximum_speed, tank_volume_liters):
            super().__init__(registration_number, maximum_speed)
            self.tank_volume_liters = tank_volume_liters


def display_publication_information():
    donald_duck_magazine = Exc.Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6_book = Exc.Book("Compartment No. 6", "Rosa Liksom", 192)
    print("--- Magazine Information ---")
    donald_duck_magazine.print_information()
    print("\n--- Book Information ---")
    compartment_no_6_book.print_information()


def simulate_electric_car():
    electric_car = Exc.ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = Exc.GasolineCar("ACD-123", 165, 32.3)
    electric_car.current_speed = 120
    gasoline_car.current_speed = 110
    electric_car.drive(3)
    gasoline_car.drive(3)
    print(electric_car)
    print(gasoline_car)


if __name__ == "__main__":
    function_driver(__file__)