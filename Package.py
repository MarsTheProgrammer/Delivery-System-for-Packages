# As per the requirements:
# Marshall Christian 001520145



from datetime import timedelta

class Package(object):
    EOD_TIMESTAMP = timedelta(hours=17)
    SPECIAL_PACKAGES = [13, 15, 19]
    DELIVERED = "Delivered At {}"
    EN_ROUTE = "En route, Left Hub At: {}"
    AT_HUB = "Waiting At Hub"
    DEADLINE_PACKAGES = [25, 28]
# add parameter of EARLIEST_CAN_DELIVER???
    def __init__(self, identifier, street, city, zipcode, deadline, weight, notes, destination):
        self.identifier = int(identifier)
        self.street = street
        self.destination = destination
        self.city = city
        self.zip = zipcode
        self.deadline = self.convert_to_timestamp(deadline)
        self.weight = weight
        self.notes = notes

        self.delivered_at = None
        self.package_is_ready = timedelta(hours=8)
        self.available_trucks = [1, 2]
        self.left_hub_at = None
        self.on_truck = False
        self.notes = notes

    def inline_report(self, time):
        if self.identifier == 9:
            self.street = "410 S State St"
            self.zip = 84111
        report = self.specific_package_lookup(time)
        # Formatting purposes
        return report[1:].replace("\n", "   ")

    # Formatting for the report that is used when looking up information about a package.
    def specific_package_lookup(self, time = timedelta(hours=17)):
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
            self.identifier,
            self.street,
            self.city,
            self.zip,
            self.deadline_method(),
            self.weight,
            self.delivery_status_method(time)
        )

    # Used for packages with deadlines
    def has_deadline(self):
        return self.deadline != self.EOD_TIMESTAMP

    # Used for packages with deadlines
    def deadline_method(self):
        if self.deadline == self.EOD_TIMESTAMP:
            return "{} (EOD)".format(self.deadline)

    # Figures out if the package is top priority by manually loading
    def is_top_priority(self):
        return self.identifier == 1 or 13 or 14 or 15 or 16 or 19 or 20 or 29 or 31 or 34 or 37 or 40 or 39 or 35 or 8 or 30 or \
               36 or 38 or 18 or 3 or 33 or 32 or 27 or 6 or 25 or 26 or 24 or 23 or 22 or 21 or 17 or 28 or \
                                  9 or 11 or 10 or 12 or 7 or 5 or 4 or 2

    # Finds delivery status by the time passed in
    def delivery_status_method(self, time):
        if time > self.delivered_at:
            return self.DELIVERED.format(self.delivered_at)
        elif time > self.left_hub_at:
            return self.EN_ROUTE.format(self.left_hub_at)

        return self.AT_HUB

    # Converts the time_string to a timestamps that is usable
    def convert_to_timestamp(self, time_string):
        if time_string == "EOD":
            return self.EOD_TIMESTAMP
        (hour, minute, sec) = time_string.split(":")
        return timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))
