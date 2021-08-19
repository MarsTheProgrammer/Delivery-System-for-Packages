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

        # Lists
        all_packages = []
        top_priority = []
        bottom_priority = []

        # This will loop through the PackageInformation file and create the three lists from above: all packages, top and bottom priority
        with open("PackageInformation.csv") as csvfile:
            package_info = csv.reader(csvfile)

            for row in package_info:
                package = Package(*(row + [locations_hash.look_up(row[1])]))

                all_packages.append(package)
                packages_hash.insert(package.identifier, package)

                # Here the packages are separated into top and bottom priority lists. Dependant upon deadlines and special instructions
                # Time complexity: O(1) because it is an append
                if package.is_top_priority():
                    top_priority.append(package)
                else:
                    bottom_priority.append(package)

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
        start_location = locations_hash.look_up(0)

        # There will only be 2 trucks. The first truck will travel twice.
        truck_list = [Truck(1, start_time, start_location), Truck(2, start_time, start_location)]

        # List of the time when trucks need to wait to leave the hub. Used for optimization
        times_to_leave_hub = [
            timedelta(hours=8),
            timedelta(hours=9, minutes=5),
            timedelta(hours=10, minutes=20)
        ]

        # Sorts the top and bottom priority lists based on distance from the hub
        # Time & Space complexity: O(n)
        top_priority = sorted(top_priority, key=graph.distance_to_deliver(start_location))
        bottom_priority = sorted(bottom_priority, key=graph.distance_to_deliver(start_location))

        count = 0
        truck_index = 0
        first_row = 0

        # While loop to end when all packages are delivered
        while count < len(all_packages):
            truck = truck_list[truck_index]

            if first_row < len(times_to_leave_hub):
                leave_hub_at = times_to_leave_hub[first_row]
                truck.wait_at_hub(leave_hub_at)

            # Filter priority lists on which packages the truck can deliver
            # Time & Space complexity: O(n)
            filtered_top = [pack for pack in top_priority if truck.can_deliver(pack)]
            # Takes all the top priority packages the truck can fit
            # Time & Space complexity: O(1) because it is an append
            for package in filtered_top:
                truck.add_package(package)
                count += 1

                if truck.is_full():
                    break

            # If is not full, fill it with low priority packages
            if truck.is_full() is not True:
                filtered_low = [pack for pack in bottom_priority if truck.can_deliver(pack)]
                for package in filtered_low:
                    truck.add_package(package)
                    count += 1

                    if truck.is_full():
                        break

            # Truck delivers the packages using the delivering_packages_algo algorithm to find the best path through graph
            # Time & Space complexity: O(n^2)
            truck.delivering_packages_algo(graph, (len(all_packages) - count) > truck.max)
            first_row += 1
            truck_index = first_row % len(truck_list)

        # Finds the total distance of truck
        def total_distance(truck):
            return truck.total_distance

        return [sum(map(total_distance, truck_list)), packages_hash, all_packages]
