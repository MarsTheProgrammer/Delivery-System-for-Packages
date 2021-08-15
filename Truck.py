# As per the requirements:
# Marshall Christian 001520145

from datetime import timedelta

class Truck(object):
    MAX_PACKAGES_PER_TRUCK = 16
    SPEED_OF_TRUCK = 18.0
    SECONDS_PER_HOUR = 3600.0

    # Variables for the truck object:
    def __init__(self, identifier, start_time, start_location):
        self.identifier = identifier
        self.current_time = start_time
        self.start_location = start_location
        self.total_distance = 0
        self.max = self.MAX_PACKAGES_PER_TRUCK
        self.packages = []
        self.locations = set()

    # This adds the packages to package list. Then, the package location to a location set
    # Time Complexity: O(n) - 'n' being the number of packages
    def add_package(self, package):
        # If the packages is less than the MAX_PACKAGES_PER_TRUCK, add package to list.
        if len(self.packages) < self.max:
            self.packages.append(package)
            self.locations.add(package.destination)

            # Let it know the package is on the truck and @ what time
            package.on_truck = True
            package.left_hub_at = self.current_time


    # Checks to see of truck is full
    def is_full(self):
        return len(self.packages) == self.max

    # Simple helper method to get time @ hub
    def wait_at_hub(self, timestamp):
        self.current_time = timestamp

    # can_deliver() figures out of a truck has the ability to deliver the specified package
    # Checks to see if package on one of the other trucks. Checks if can be delivered by that truck number, or if the package is ready
    def can_deliver(self, package):
        return not package.on_truck and self.identifier in package.truck_availability and self.current_time >= package.ready_at


    # This is a greedy algorithm
    # delivering_packages_algo takes a couple of parameters. A map of the city and a boolean of returning to the hub.
    # Here is what it does: sorts the packages list by distance of trucks current location after the truck had traveled.
    # After doing this, it will update the list based on the new location. This will continue until all packages are delivered
    # Time complexity: O(n^2) with 'n' being the number of packages
    def delivering_packages_algo(self, map_of_city, return_to_hub=True):
        current_location = self.start_location
        locations = list(self.locations)

        while self.packages:
            # This will sort the locations by distance to current location and pop nearest location off.
            # Time complexity: O(n)
            locations = sorted(locations, key=map_of_city.distance_from(current_location))
            nearest_location = locations.pop(0)

            distance = map_of_city.find_distance_between(current_location, nearest_location)
            time_to_deliver = self.traveling_time(distance)
            delivered_at = self.current_time + timedelta(seconds=time_to_deliver)

            # Finds all packages that need to be delivered at current location. In case there are multiple for optimization
            # Time complexity: O(n)
            packages_at_location = [p for p in self.packages if p.destination.identifier == nearest_location.identifier]
            for package in packages_at_location:
                package.delivered_at = delivered_at

                # Removes package from list
                # Time complexity: O(n)
                self.packages.remove(package)

            # This will update location, time, and total distance the truck traveled
            current_location = nearest_location
            self.total_distance += distance
            self.current_time = delivered_at

        # This is needed in case the truck is out of packages and needs to return to the hub.
        if return_to_hub:
            distance = map_of_city.find_distance_between(current_location, self.start_location)
            time_to_return = self.traveling_time(distance)

            self.current_time = self.current_time + timedelta(seconds=time_to_return)
            self.total_distance += distance

            # ensure the locations list is empty before adding more packages
            self.locations = set()

    # Helps get distance in terms of traveling time
    def traveling_time(self, distance):
        return (distance / self.SPEED_OF_TRUCK) * self.SECONDS_PER_HOUR
