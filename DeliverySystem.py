# As per the requirements:
# Marshall Christian 001520145

import csv
from datetime import timedelta
from Package import Package
from Location import Location
from HashTable import HashTable
from Graph import Graph
from Truck import Truck

class PackageDelivery(object):
    @staticmethod
    # Run is the main function that executes the entire package delivery program
    def run():
        graph = Graph()
        locations_hash = HashTable(20)
        packages_hash = HashTable(40)

        # Loading DistanceName data from the csv file and populating the hash table and graph with location data
        with open("DistanceName.csv") as csvfile:
            distance_name = csv.reader(csvfile)

            # Time to loop through the location data
            # Time & Space complexity: O(n)
            for row in distance_name:
                location = Location(*row)

                # Inserting location data into hash table
                # Time complexity: O(n)
                locations_hash.insert(location.identifier, location)
                locations_hash.insert(location.address, location)

                # Creating vertexes on graph from location data
                # Time complexity: O(n)
                graph.add_vertex(location)

        # Lists of packages
        all_packages = []
        truck_one_trip_one = []
        truck_two_trip_one = []
        truck_one_trip_two = []

        # This will loop through the PackageInformation file and create the three lists from above: all packages, top and bottom priority
        with open("PackageInformation.csv") as csvfile:
            package_info = csv.reader(csvfile)

            for row in package_info:
                package = Package(*(row + [locations_hash.look_up(row[1])]))

                all_packages.append(package)
                packages_hash.insert(package.identifier, package)

                # Here the packages are separated into manually loaded lists
                # Time complexity: O(1) because it is an append
                if package.truck_one_trip_one():
                    truck_one_trip_one.append(package)
                if package.truck_two():
                    truck_two_trip_one.append(package)
                if package.truck_one_trip_two():
                    truck_one_trip_two.append(package)

        # This will loop through the DistanceTable file and sort the data between locations.
        # The data will then be used to create the weighted edges between vertexes in the graph
        with open("DistanceTable.csv") as csvfile:
            distance_table = csv.reader(csvfile)

            # Loops through every cell in DistanceTable file
            # Time & Space complexity: O(n^2)
            for first_row, row in enumerate(distance_table):
                for second_row, data in enumerate(row):
                    if data != '':
                        # Adds weighted edge to graph
                        # Time complexity: O(n)
                        graph.add_weighted_edge(locations_hash.look_up(first_row),
                                                locations_hash.look_up(second_row),
                                                float(data))

        start_time = timedelta(hours=8)
        start_time_truck_2 = timedelta(hours=9, minutes=5)
        start_location = locations_hash.look_up(0)

        # There will only be 2 trucks. The first truck will travel twice.
        truck_list = [Truck(1, start_time, start_location), Truck(2, start_time_truck_2, start_location)]
        truck1 = Truck(1, start_time, start_location)
        truck2 = Truck(2, start_time_truck_2, start_location)
        # List of the time when trucks need to wait to leave the hub
        times_to_leave_hub = [timedelta(hours=8), timedelta(hours=9, minutes=5), timedelta(hours=10, minutes=20)]

        # Sorts the lists based upon distances
        # Time & Space complexity: O(n)
        truck_one_trip_one = sorted(truck_one_trip_one, key=graph.distance_to_deliver(start_location))
        truck_two_trip_one = sorted(truck_two_trip_one, key=graph.distance_to_deliver(start_location))
        truck_one_trip_two = sorted(truck_one_trip_two, key=graph.distance_to_deliver(start_location))

        count = 0
        first_row = 0

        if first_row <= len(times_to_leave_hub):
            leave_hub_at = times_to_leave_hub[first_row]
            truck1.wait_at_hub(leave_hub_at)
        first_row += 1

        # Takes all the packages the truck can fit on first trip
        # Time & Space complexity: O(1) because it is an append
        for package in truck_one_trip_one:
            truck1.add_package(package)
            count += 1

        truck1.delivering_packages_algo(graph, (len(all_packages) - count) > truck1.max)

        # Takes all the packages the truck can fit on first trip
        # Time & Space complexity: O(1) because it is an append
        for package in truck_two_trip_one:
            truck2.add_package(package)
            count += 1

        truck2.delivering_packages_algo(graph, (len(all_packages) - count) > truck2.max)


        # Takes all the packages the truck can fit on first trip
        # Time & Space complexity: O(1) because it is an append
        for package in truck_one_trip_two:
            truck1.add_package(package)
            count += 1

        truck1.delivering_packages_algo(graph, (len(all_packages) - count) > truck1.max)

        # Finds the total distance of truck1 & truck2, including all trips
        def total_distance(truck2):
            return truck1.total_distance + truck2.total_distance

        return [sum(map(total_distance, truck_list)), packages_hash, all_packages]
