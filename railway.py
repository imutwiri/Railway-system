import sqlite3

# Create a connection to the database
conn = sqlite3.connect('sgr_database.db')
c = conn.cursor()

# Create a table for trains
c.execute('''CREATE TABLE IF NOT EXISTS trains
             (train_id INTEGER PRIMARY KEY,
              train_name TEXT NOT NULL,
              origin TEXT NOT NULL,
              destination TEXT NOT NULL,
              departure_time TEXT NOT NULL,
              arrival_time TEXT NOT NULL)''')

# Create a table for passengers
c.execute('''CREATE TABLE IF NOT EXISTS passengers
             (passenger_id INTEGER PRIMARY KEY,
              passenger_name TEXT NOT NULL,
              phone_number TEXT NOT NULL,
              train_id INTEGER,
              FOREIGN KEY (train_id) REFERENCES trains(train_id))''')

# Function to add a train to the database
def add_train(train_name, origin, destination, departure_time, arrival_time):
    c.execute("INSERT INTO trains (train_name, origin, destination, departure_time, arrival_time) VALUES (?, ?, ?, ?, ?)",
              (train_name, origin, destination, departure_time, arrival_time))
    conn.commit()
    print("Train added successfully.")

# Function to add a passenger to the database
def add_passenger(passenger_name, phone_number, train_id):
    c.execute("INSERT INTO passengers (passenger_name, phone_number, train_id) VALUES (?, ?, ?)",
              (passenger_name, phone_number, train_id))
    conn.commit()
    print("Passenger added successfully.")

# Function to get all trains
def get_trains():
    c.execute("SELECT * FROM trains")
    trains = c.fetchall()
    return trains

# Function to get all passengers for a given train
def get_passengers(train_id):
    c.execute("SELECT * FROM passengers WHERE train_id=?", (train_id,))
    passengers = c.fetchall()
    return passengers

# Example usage
add_train("SGR001", "Nairobi", "Mombasa", "8:00 AM", "4:00 PM")
add_train("SGR002", "Nairobi", "Nakuru", "10:00 AM", "12:00 PM")

add_passenger("Ian Mutwiri", "1234567890", 1)
add_passenger("Stephen Gachoka", "9876543210", 2)

trains = get_trains()
passengers = get_passengers(1)

print("Trains:")
for train in trains:
    print(train)

print("\nPassengers for Train 1:")
for passenger in passengers:
    print(passenger)

# Close the database connection
conn.close()