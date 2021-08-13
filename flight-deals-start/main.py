# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import datetime
from datetime import timedelta
from notification_manager import NotificationManager

sheety_endpoint = "https://api.sheety.co/801d627059cb6f98e7e3e9308b47a1b3/flightDeals/prices"
ORIGIN_CITY_IATA = "PHL"

d_manager = DataManager()
sheet_data = d_manager.get_destination_data()  # gets all data from sheets
flight_search = FlightSearch()
notification_manager =NotificationManager()

pprint(sheet_data)  #dict inside a list

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    # city_names =[row["city"] for row in sheet_data]
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])  # gets the city code and inserts in the data
    print(sheet_data)
    d_manager.destination_data = sheet_data
    d_manager.update_destination_codes()  # puts the codes in Sheety

tomorrow = datetime.datetime.now() + timedelta(days=1)
six_month_from_today = datetime.datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time= tomorrow,
        to_time= six_month_from_today,
    )
    """to check if any of the flights found
     are cheaper than the Lowest Price listed in 
     the Google Sheet. If so, then we should use the Twilio API to send an SMS
    """
    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
