# As per the requirements:
# Marshall Christian 001520145

# This was also made possible by the same people in the Graph.py

from HashTable import HashTable

class Vertex(object):
    def __init__(self, location):
        self.edges = HashTable()
        self.value = location

    # Adds edge to hash table
    # Time & Space complexity: O(n)
    def add_edge(self, edge):
        self.edges.insert(edge.identifier, edge)

    # Finds distance to a nearby vertex
    # Time & Space complexity: O(n)
    def distance_to_nearby(self, location):
        return self.edges.look_up(location.identifier).weight

    # Finds edge from ID
    # Time & Space complexity: O(n)
    def find_edge(self, edge_id):
        return self.edges.look_up(edge_id)
