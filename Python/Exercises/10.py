from main import function_driver
import random


class Exc:
    class Elevator:
        def __init__(self, bottom, top):
            self.current_floor = bottom
            self.bottom_floor = bottom
            self.top_floor = top

        def go_to_floor(self, desired_floor):
            if desired_floor > self.top_floor or desired_floor < self.bottom_floor:
                print(f"Floor {desired_floor} is out of range!")
                return

            print(f"Moving to floor {desired_floor}...")
            while self.current_floor != desired_floor:
                if self.current_floor < desired_floor:
                    self.floor_up()
                else:
                    self.floor_down()
            print(f"Arrived at floor {self.current_floor}.")

        def floor_up(self):
            if self.current_floor < self.top_floor:
                self.current_floor += 1
                print(f"Floor up, current floor: {self.current_floor}")
            else:
                print("Reached the top floor. Can't go up!")

        def floor_down(self):
            if self.current_floor > self.bottom_floor:
                self.current_floor -= 1
                print(f"Floor down, current floor: {self.current_floor}")
            else:
                print("Reached the bottom floor. Can't go down!")

    class Building:
        def __init__(self, bottom, top, num_elevators):
            self.bottom = bottom
            self.elevators = [Exc.Elevator(bottom, top) for _ in range(num_elevators)]

        def run_elevator(self, elevator_number, destination_floor):
            if elevator_number < 1 or elevator_number > len(self.elevators):
                print(f"No such elevator: {elevator_number}! Elevator numbers start from 1.")
                return

            selected_elevator = self.elevators[elevator_number - 1]
            selected_elevator.go_to_floor(destination_floor)

        def fire_alarm(self):
            print("Fire alarm! All elevators are moving to the bottom floor.")
            for i, elevator in enumerate(self.elevators, start=1):
                print(f"\nMoving elevator {i} to the bottom floor...")
                elevator.go_to_floor(self.bottom)

    # Car and Race classes from the second scenario
    class Car:
        def __init__(self, registration_number, maximum_speed):
            self.registration_number = registration_number
            self.maximum_speed = maximum_speed
            self.current_speed = 0
            self.travelled_distance = 0

        def update_speed(self, speed_change):
            new_speed = self.current_speed + speed_change
            self.current_speed = max(0, min(new_speed, self.maximum_speed))

        def drive(self, hours):
            speed_change = random.randint(-10, 15)
            self.update_speed(speed_change)
            distance = self.current_speed * hours
            self.travelled_distance += distance

        def __str__(self):
            reg_number_str = f"{self.registration_number:<20}"
            max_speed_str = f"{self.maximum_speed:<20}"
            current_speed_str = f"{self.current_speed:<25}"
            travelled_distance_str = f"{self.travelled_distance:<20}"

            return f"{reg_number_str}{max_speed_str}{current_speed_str}{travelled_distance_str}"

    class Race:
        def __init__(self, name, kilometers, cars):
            self.name = name
            self.distance = kilometers
            self.cars = cars

        def simulate_hour(self):
            for car in self.cars:
                speed_change = random.randint(-10, 15)
                car.update_speed(speed_change)
                car.drive(1)

        def hour_passes(self):
            self.simulate_hour()

        def print_status(self):
            print(f"\nCurrent status of the race '{self.name}':")
            print(
                f"{'Registration No.':<20}{'Max Speed (km/h)':<20}{'Current Speed (km/h)':<25}{'Travelled Distance (km)':<25}")
            for car in self.cars:
                print(
                    f"{car.registration_number:<20}{car.maximum_speed:<20}{car.current_speed:<25}{car.travelled_distance:<25}")

        def race_finished(self):
            return any(car.travelled_distance >= self.distance for car in self.cars)


def run_elevator_emergency_drill():
    building = Exc.Building(1, 10, 3)

    print("Elevator 1 is going to floor 6.")
    building.run_elevator(1, 6)

    print("Elevator 2 is going to floor 8.")
    building.run_elevator(2, 8)

    print("Elevator 3 is going to floor 3.")
    building.run_elevator(3, 3)

    print("\n--- Fire alarm triggered! ---")
    building.fire_alarm()


def simulate_car_race():
    RACE_DISTANCE = 8000
    NUM_CARS = 10
    cars = [Exc.Car(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(NUM_CARS)]
    race = Exc.Race("Grand Demolition Derby", RACE_DISTANCE, cars)

    print(f"\nStarting the race: {race.name}\n")
    hours_passed = 0

    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1
        if hours_passed % 10 == 0 or race.race_finished():
            race.print_status()

    print("Race concluded.\n")


if __name__ == "__main__":
    function_driver(__file__)
