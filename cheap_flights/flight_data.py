class FlightData:
    def __init__(self, origin, destination, out, ret, price=None):
        self.price = price
        self.origin_airport = origin
        self.destination_airport = destination
        self.out_date = out
        self.return_date = ret

    def print_flightdata(self):
        print(f"Price:  {self.price}")
        print(f"Origin: {self.origin_airport}")
        print(f"Destination: {self.destination_airport}")
        print(f"Out:  {self.out_date}")
        print(f"Return:  {self.return_date}")


def find_cheapest_flight(data, return_date):
    cheapest_flight = None
    low_price = float("inf")

    for flight in data["best_flights"]:
        if flight["price"] < low_price:
            cheapest_flight = FlightData(
                origin=flight["flights"][0]["departure_airport"]["id"],
                destination=flight["flights"][-1]["arrival_airport"]["id"],
                out=flight["flights"][0]["departure_airport"]["time"].split(" ")[0],
                ret=return_date,
                price=flight["price"],
            )
            low_price = flight["price"]
        # print(flight["price"])
    for flight in data["other_flights"]:
        if flight["price"] < low_price:
            cheapest_flight = FlightData(
                origin=flight["flights"][0]["departure_airport"]["id"],
                destination=flight["flights"][-1]["arrival_airport"]["id"],
                out=flight["flights"][0]["departure_airport"]["time"].split(" ")[0],
                ret=return_date,
                price=flight["price"],
            )
            low_price = flight["price"]
        # print(flight["price"])
    return cheapest_flight
