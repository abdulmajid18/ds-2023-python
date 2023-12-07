class UndergroundSystem:

    def __int__(self):
        self.check_in_map = {}
        self.total_map = {}

    def checkIn(self, id, station_name, time):
        self.check_in_map[id] = (station_name, time)

    def checkOut(self, id, station_name, t):
        start, time = self.check_in_map[id]
        route = (start, station_name)
        if route not in self.total_map:
            self.total_map[route] = [0, 0]
        self.total_map[route][0] = t - time
        self.total_map[route][1] += 1

    def getAverageTime(self, start, end):
        total, count = self.total_map[(start, end)]
        return total / count


class UndergroundSystem2:
    def __init__(self):
        # Dictionary to store customer check-ins.
        self.check_ins = {}
        # Dictionary to store station-to-station travel times.
        self.travel_times = {}

    def checkIn(self, customer_id, station_name, timestamp):
        # Store check-in information in the check_ins dictionary.
        self.check_ins[customer_id] = (station_name, timestamp)

    def checkOut(self, customer_id, station_name, timestamp):
        # Retrieve check-in information.
        start_station, start_time = self.check_ins[customer_id]

        # Calculate travel time.
        travel_time = timestamp - start_time

        # Update travel times dictionary.
        if (start_station, station_name) not in self.travel_times:
            self.travel_times[(start_station, station_name)] = [travel_time, 1]
        else:
            self.travel_times[(start_station, station_name)][0] += travel_time
            self.travel_times[(start_station, station_name)][1] += 1

        # Remove check-in record.
        del self.check_ins[customer_id]

    def getAverageTime(self, start_station, end_station):
        # Calculate and return the average travel time between two stations.
        total_time, total_trips = self.travel_times.get((start_station, end_station), [0, 0])
        if total_trips == 0:
            return 0
        return total_time / total_trips
