# As per the requirements:
# Marshall Christian 001520145

from HashTable import HashTable

class Vertex(object):
    def __init__(self, location):
        self.edges = HashTable()
        self.value = location

    # Adds edge to hash table
    # Time complexity: O(n)
    def add_edge(self, edge):
        self.edges.insert(edge.identifier, edge)

    # Finds edge from ID
    # Time complexity: O(n)
    def find_edge(self, edge_id):
        return self.edges.find(edge_id)

    # Finds distance to a nearby vertex
    # Time complexity: O(n)
    def distance_to_nearby(self, location):
        return self.edges.find(location.identifier).weight
