import requests


def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # import ipdb; ipdb.set_trace() # esto es un breakpoint para debuggear y ver el valor de las variables
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }
