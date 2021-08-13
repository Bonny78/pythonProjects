import requests
from flight_data import FlightData

TEQUILA_API_KEY = "hOrA1eXo2gsoJaWJMnu2OhVJ6eID1nPg"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_FLIGHT_SEARCH_KEY = "hOrA1eXo2gsoJaWJMnu2OhVJ6eID1nPg"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    # this method retrieves the city code from url
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        params = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_FLIGHT_SEARCH_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                headers=headers,
                                params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        # fetching only the data I need and storing it in
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][0]["local_arrival"].split("T")[0],
        )

        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
