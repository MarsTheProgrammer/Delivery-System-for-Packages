# As per the requirements:
# Marshall Christian 001520145

# This was also made possible by the same people in the Graph.py

# Location class used in the graph
# Has 3 variables: location, name, and address
class Location(object):
    def __init__(self, identifier, name, address):
        self.identifier = int(identifier)
        self.name = name
        self.address = address