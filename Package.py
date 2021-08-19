# As per the requirements:
# Marshall Christian 001520145



from datetime import timedelta

class Package(object):
    EOD_TIMESTAMP = timedelta(hours=17)
    SPECIAL_PACKAGES = [13, 15, 19]
    DELIVERED = "Delivered At {}"
    EN_ROUTE = "En route, Left Hub At: {}"
    AT_HUB = "Waiting At Hub"

    def __init__(self, identifier, street, city, zipcode, deadline, weight, notes, destination):
        self.identifier = int(identifier)
        self.street = street
        self.destination = destination
        self.city = city
        self.zip = zipcode
        self.deadline = self.convert_to_timestamp(deadline)
        self.weight = weight
        self.notes = notes
        self.modify(notes=notes)

        self.delivered_at = None
        self.package_is_ready = timedelta(hours=8)
        self.truck_availability = [1, 2]
        self.left_hub_at = None
        self.on_truck = False
        self.notes = notes

    def inline_report(self, time):
        report = self.specific_package_lookup(time)
        # Formatting purposes
        return report[1:].replace("\n", "   ")

    # Formatting for the report that is used when looking up information about a package.
    def specific_package_lookup(self, time = timedelta(hours=17)):
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

        return "{}".format(self.deadline)

    # Figures out if the package is top priority by deadline or special instructions
    def is_top_priority(self):
        return self.has_deadline() or self.notes != "None" or self.identifier in self.SPECIAL_PACKAGES

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

    # Changes package state based on special instructions
    def modify(self, notes):
        if notes == ("Wrong address listed", notes):
            self.package_is_ready = timedelta(hours=10, minutes=20, seconds=00)
            self.street = "410 S State St"
            self.zip = 84111
        elif notes == ("Delayed", notes):
            self.package_is_ready = timedelta(hours=9, minutes=5, seconds=00)
        elif notes == ("Can only be on truck 2", notes):
            self.truck_availability = [2]
