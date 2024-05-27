class Train:
    def __init__(self, train_id, name, source, destination):
        self.train_id = train_id
        self.name = name
        self.source = source
        self.destination = destination

class Station:
    def __init__(self, station_id, name):
        self.station_id = station_id
        self.name = name

class Passenger:
    def __init__(self, passenger_id, name, train_id, source, destination):
        self.passenger_id = passenger_id
        self.name = name
        self.train_id = train_id
        self.source = source
        self.destination = destination

class RailwayDatabase:
    def __init__(self):
        self.trains = []
        self.stations = []
        self.passengers = []

    def add_train(self, train):
        self.trains.append(train)

    def add_station(self, station):
        self.stations.append(station)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def display_trains(self):
        print("Trains:")
        for train in self.trains:
            print(f"Train ID: {train.train_id}, Name: {train.name}, Source: {train.source}, Destination: {train.destination}")

    def display_stations(self):
        print("Stations:")
        for station in self.stations:
            print(f"Station ID: {station.station_id}, Name: {station.name}")

    def display_passengers(self):
        print("Passengers:")
        for passenger in self.passengers:
            print(f"Passenger ID: {passenger.passenger_id}, Name: {passenger.name}, Train ID: {passenger.train_id}, Source: {passenger.source}, Destination: {passenger.destination}")

# Example usage:
if __name__ == "__main__":
    db = RailwayDatabase()

    t1 = Train(1, "Express", "StationA", "StationB")
    t2 = Train(2, "Local", "StationB", "StationC")
    db.add_train(t1)
    db.add_train(t2)

    s1 = Station(1, "StationA")
    s2 = Station(2, "StationB")
    s3 = Station(3, "StationC")
    db.add_station(s1)
    db.add_station(s2)
    db.add_station(s3)

    p1 = Passenger(1, "Alice", 1, "StationA", "StationB")
    p2 = Passenger(2, "Bob", 2, "StationB", "StationC")
    db.add_passenger(p1)
    db.add_passenger(p2)

    db.display_trains()
    db.display_stations()
    db.display_passengers()
