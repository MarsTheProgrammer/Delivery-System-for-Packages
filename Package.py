# As per the requirements:
# Marshall Christian 001520145


from datetime import timedelta


def deadline_to_time(deadline_column):
    if deadline_column != "EOD":
        (hour, minute, sec) = deadline_column.split(":")
        return timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))


class Package(object):
    delivered_status = "Delivered At {}"
    en_route = "En route, left Hub At: {}"
    at_hub_waiting = "Waiting At Hub"

    def __init__(self, identifier, street, city, zipcode, deadline, weight, notes, destination):
        self.identifier = int(identifier)
        self.street = street
        self.destination = destination
        self.city = city
        self.zip = zipcode
        self.deadline = deadline_to_time(deadline)
        self.weight = weight
        self.notes = notes

        self.delivered_at = None
        self.available_trucks = [1, 2]
        self.left_hub_at = None
        self.on_truck = False
        self.notes = notes

    def inline_report(self, time):
        if self.identifier == 9:
            self.street = "410 S State St"
            self.zip = 84111
        report = self.specific_package_lookup(time)
        # Formatting purposes used StackOverflow
        return report[1:].replace("\n", "   ")

    # Formatting for the report that is used when looking up information about a package.
    def specific_package_lookup(self, time=timedelta(hours=17)):
        if self.identifier == 9:
            self.street = "410 S State St"
            self.zip = 84111
        return """
    ID: {}
    Address: {} {} UT
    Zipcode: {}
    Deadline: {}
    Weight: {}
    Delivery Status: {}\
""".format(
            self.identifier, self.street, self.city, self.zip, self.deadline, self.weight,
            self.delivery_status_method(time)
        )

    # Manual load of first truck trip 1
    def truck_one_trip_one(self):
        if self.identifier == 1 or self.identifier == 13 or self.identifier == 14 or self.identifier == 15 or self.identifier == 16 or self.identifier == 19 or self.identifier == 20 or self.identifier == 29 or self.identifier == 31 or self.identifier == 34 or self.identifier == 37 or self.identifier == 40 or self.identifier == 39 or self.identifier == 35 or self.identifier == 8 or self.identifier == 30:
            return self.identifier

    # Manual load of second truck
    def truck_two(self):
        return self.identifier == 36 or self.identifier == 38 or self.identifier == 18 or self.identifier == 3 or self.identifier == 33 or self.identifier == 32 or self.identifier == 27 or self.identifier == 6 or self.identifier == 25 or self.identifier == 26 or self.identifier == 24 or self.identifier == 23 or self.identifier == 22 or self.identifier == 21 or self.identifier == 17 or self.identifier == 28

    # Manual load of first truck trip 2
    def truck_one_trip_two(self):
        return self.identifier == 9 or self.identifier == 11 or self.identifier == 10 or self.identifier == 12 or self.identifier == 7 or self.identifier == 5 or self.identifier == 4 or self.identifier == 2

    # Finds delivery status by the time passed in
    def delivery_status_method(self, time):
        if time > self.delivered_at:
            return self.delivered_status.format(self.delivered_at)
        elif time > self.left_hub_at:
            return self.en_route.format(self.left_hub_at)

        return self.at_hub_waiting
