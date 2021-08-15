# As per the requirements:
# Marshall Christian 001520145

# Edge class used in the graph
# Has 3 variables: location, identifier, and weight
class Edge(object):
    def __init__(self, location, weight=0.0):
        self.location = location
        self.identifier = location.identifier
        self.weight = weight
