import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/801d627059cb6f98e7e3e9308b47a1b3/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data ={}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        result = response.json()
        self.destination_data = result["prices"]

        return self.destination_data

#this method puts the code in the sheet
    def update_destination_codes(self):
        for city in self.destination_data:
            param ={
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response =requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                                   json=param)
            print(response.text)