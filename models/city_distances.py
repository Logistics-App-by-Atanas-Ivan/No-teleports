import csv

class CityDistances:
    def __init__(self):
        self._csv_file ="core/data files/Logistics_App(City Distances).csv"
        self._cities=[]
        self._distances=[]

        with open(self._csv_file, newline="") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        self._cities = rows[0][1:]

        for row in rows[1:]:
            self._distances.append([int(x) for x in row[1:]])


    def calculate_distance(self, end_location, route):
        route_locations = route.locations
        distance = 0 

        for x in range(1, len(route.locations)):

            distance += self._distances [self._cities.index(route.locations[x-1])] [self._cities.index(route.locations[x])]

            if route.locations[x]==end_location:
                return distance

            


    
