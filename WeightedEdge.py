# As per the requirements:
# Marshall Christian 001520145

# This was also made possible by the same people in the Graph.py

# Edge class used in the graph
# Has 3 variables: location, identifier, and weight
class Edge(object):
    def __init__(self, location, weight=0.0):
        self.identifier = location.identifier
        self.location = location
        self.weight = weight
