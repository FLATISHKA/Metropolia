from main import function_driver
import random


class Exc:
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
            reg_number_str = f"{self.registration_number:<20}"
            max_speed_str = f"{self.maximum_speed:<20}"
            current_speed_str = f"{self.current_speed:<25}"
            travelled_distance_str = f"{self.travelled_distance:<20}"

            return f"{reg_number_str}{max_speed_str}{current_speed_str}{travelled_distance_str}"


def simulate_car_race():
    cars = []
    race_distance = 10000
    number_of_cars = 10

    for i in range(1, number_of_cars + 1):
        max_speed = random.randint(100, 200)
        cars.append(Exc.Car(f"ABC-{i}", max_speed))

    while True:
        for car in cars:
            car.drive(1)
            if car.travelled_distance >= race_distance:
                print("Race is over.")
                break
        else:
            continue
        break

    print(
        f"{'Registration No.':<20}{'Max Speed (km/h)':<20}{'Current Speed (km/h)':<25}{'Travelled Distance (km)':<20}")
    for car in cars:
        print(str(car))


if __name__ == "__main__":
    function_driver(__file__)
