#   TÄSSÄ ODOTTAA SUA BIG SUPRISE
#    EI SAA KATTOA ENNE KLO 4:00
#        MUUTEN KONELLE KAPUT.



def read_data(filename):
    with open(filename, 'r') as file:
        return {line.split(';')[0].strip(): list(map(int, line.split(';')[1].split(','))) for line in file}


def find_best_time(data, day, earliest, latest):
    times = data.get(day, [])
    earliest_idx, latest_idx = earliest - 7, latest - 7
    min_time, min_people = earliest_idx, times[earliest_idx]

    for time, count in enumerate(times[earliest_idx:latest_idx + 1], start=earliest_idx):
        if count <= min_people:
            min_time, min_people = time, count

    return min_time + 7


def get_input_within_range(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            # jos toi ei käy, poistaa hemmettiin ja laita tähän tilalle (raise) niinku rivillä 28
            print(f"Please enter a value between {low} and {high}.")
        except ValueError:
            print("Invalid time. Program ends.")
            raise


def main():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    day = input("Enter the day which you want to go to the gym 'Mon, Tue, Wed, Thu, Fri, Sat or Sun':\n")
    if day not in days:
        print("Day not found in the list.")
        return

    try:
        file_name = input("Enter the filename:\n")
        data = read_data(file_name)
        with open(file_name, 'r') as file:
            days = [line.split(';')[0].strip() for line in file]
        print(days)
        days = ", ".join(days)
        print(f"....'{days}'")
    except FileNotFoundError:
        print(f"Error in reading the file {file_name}. Program ends.")
        return

    try:
        earliest = get_input_within_range("Enter your earliest desired time (7-22):\n", 7, 22)
        latest = get_input_within_range("Enter your latest desired time (7-22):\n", 7, 22)
    except:
        return

    best_time = find_best_time(data, day, earliest, latest)
    print(f"The best time is at {best_time}:00.")


main()
