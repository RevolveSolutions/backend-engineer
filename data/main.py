# ================================================================
# Filename: main.py
# ================================================================

# Imports
import csv
import pytest

class Revolve:
    # 1. how many total number of days does the flights table cover?
    def total_days(self, flights: str) -> int:
        '''
        Returns total number of days (unique) in flights.csv
        '''
        unique = set()
        with open(flights) as f:
            read_csv = csv.DictReader(f)
            for row in read_csv:
                date = row["day"], row["month"], row["year"]
                unique.add(date)
        return len(unique)

    # 2. how many departure cities (not airports) does the flights database cover?
    def departure_cities(self, flights: str, airports: str) -> list:
        '''
        Returns unique Departure Cities 
        '''

        dep_airports = set()
        cities = set()

        with open(flights) as f:
            read_csv = csv.DictReader(f)

            for row in read_csv:
                dep_airports.add(row["origin"])

        with open(airports) as a:
            read_csv = csv.DictReader(a)
            for row in read_csv:
                if row["IATA_CODE"] in dep_airports:
                    cities.add(row["CITY"])
        
        return list(cities)

    # 3. what is the relationship between flights and planes tables?
    def relation(self, flights: str, planes: str) -> list:
        '''
        Returns the Relationship between flights and planes
        '''
        with open(flights) as f:
            flight_read = csv.reader(f)
            fl_columns = next(flight_read)

            with open(planes) as pl:
                plane_read = csv.reader(pl)
                pl_columns = next(plane_read)

                relation = [cols for cols in pl_columns if cols in fl_columns]

        if relation: return relation
        return []

    # 4. which airplane manufacturer incurred the most delays in the analysis period?
    def most_delay_manufacturer(self, flights: str, planes: str) -> str:
        '''
        Returns manufacturer of the plane whose flights are most delayed
        '''
        delay_count = dict()
        res = ""
        with open(flights) as f:
            flight_read = csv.DictReader(f)
            for row in flight_read:
                tailnum = row["tailnum"]

                arr_delay = "".join(ch for ch in row["arr_delay"] if ch.isdigit())
                dep_delay = "".join(ch for ch in row["dep_delay"] if ch.isdigit())

                if arr_delay != "" and dep_delay != "" and int(arr_delay) > 0 and int(dep_delay) > 0:
                    delay_count[tailnum] = delay_count.get(tailnum, 0) + int(arr_delay) + int(dep_delay)
                elif arr_delay != "" and int(arr_delay) > 0:
                    delay_count[tailnum] = delay_count.get(tailnum, 0) + int(arr_delay)
                elif dep_delay != "" and int(dep_delay) > 0:
                    delay_count[tailnum] = delay_count.get(tailnum, 0) + int(dep_delay)

        sorted_delay_count = sorted(delay_count.items(), key=lambda val: val[1])

        k, N = 1, len(sorted_delay_count)
        while k < N:
            with open(planes) as pl:
                plane_read = csv.DictReader(pl)
                for row in plane_read:
                    if row["tailnum"] == sorted_delay_count[-k][0]:
                        res = row["manufacturer"]
                        k = N
            k += 1
        
        return res

    # 5. which are the two most connected cities?
    def most_connected_cities(self, flights: str, airports: str) -> list:
        '''
        Returns the Two Most Connected Cities
        '''

        connected_airport_freq = dict()
        with open(flights) as f:
            flight_read = csv.DictReader(f)
            for row in flight_read:
                key = row["origin"], row["dest"]
                connected_airport_freq[key] = connected_airport_freq.get(key, 0) + 1
            
            two_most_connected_airport = sorted(connected_airport_freq.items(), key=lambda val: val[1], reverse=True)[0]

        two_most_connected_cities = []
        with open(airports) as a:
            airport_read = csv.DictReader(a)
            for row in airport_read:
                for air in two_most_connected_airport[0]:
                    if air == row["IATA_CODE"]:
                        two_most_connected_cities.append(row["CITY"])
        
        return two_most_connected_cities


if __name__ == "__main__":
    class_obj = Revolve()

    # 1. how many total number of days does the flights table cover?
    print(class_obj.total_days("flights.csv"))                                  # Output -> 365

    # 2. how many departure cities (not airports) does the flights database cover?
    print(class_obj.departure_cities("flights.csv", "airports.csv"))            # Output -> ['New York' , 'Newark']

    # 3. what is the relationship between flights and planes tables?
    print(class_obj.relation("flights.csv", "planes.csv"))                      # Output -> ['year', 'tailnum']

    # 4. which airplane manufacturer incurred the most delays in the analysis period?
    print(class_obj.most_delay_manufacturer("flights.csv", "planes.csv"))       # Output -> EMBRAER

    # 5. which are the two most connected cities?
    print(class_obj.most_connected_cities("flights.csv", "airports.csv"))       # Output -> ['New York', 'Los Angeles']
