from main import function_driver
import requests


def chuck_norris_joke():
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()
    print(response['value'])


def weather():
    municipality = input("Municipality: ")
    api_key = 'aafc709b735e3396fd33079ce8f3255e'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        kelvin = data['main']['temp']
        celsius = kelvin - 273.15
        print(f"Weather in {municipality}: {data['weather'][0]['description']}.")
        print(f"Temperature: {celsius:.2f}°C")
    else:
        print("fetch error")


if __name__ == "__main__":
    function_driver(__file__)
