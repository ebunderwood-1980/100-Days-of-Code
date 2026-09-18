class FlightData:
    def __init__(self):
        self.price = None
        self.origin_airport = None
        self.destination_airport = None
        self.out_date = None
        self.return_date = None

    def print_flightdata(self):
        print(f"Price:  {self.price}")
        print(f"Origin: {self.origin_airport}")
        print(f"Destination: {self.destination_airport}")
        print(f"Out:  {self.out_date}")
        print(f"Return:  {self.return_date}")


def find_cheapest_flight(data, return_date):
    cheapest_flight = FlightData()
    for flight in data["best_flights"][0]:
        pass
    return cheapest_flight
