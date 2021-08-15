# As per the requirements:
# Marshall Christian 001520145

from HashTable import HashTable
from Vertex import Vertex
from WeightedEdge import Edge

class Graph(object):
    def __init__(self):
        self.vertices = HashTable(20)

    # Creates vertex from location, and add to hash table
    # Time complexity: O(n)
    def add_vertex(self, location):
        self.vertices.insert(location.identifier, Vertex(location))

    # Creates a 2 directional weighted edge between 2 vertexes
    # Time complexity: O(n)
    def add_weighted_edge(self, origin, destination, weight):
        self.vertices.find(origin.identifier).add_edge(Edge(destination, weight))
        self.vertices.find(destination.identifier).add_edge(Edge(origin, weight))

    # Finds the vertex matching the location
    # Time complexity: O(n)
    def find_vertex(self, location):
        return self.vertices.find(location.identifier)

    # Finds the distance between vertexes
    # Time complexity: O(n)
    def find_distance_between(self, origin, target):
        return self.vertices.find(origin.identifier).distance_to_nearby(target)

    # Finds distance between location and the location of the package needing delivered
    def distance_to_deliver(self, location):
        def distance_to(package):
            return self.vertices.find(location.identifier).distance_to_nearby(package.destination)

        return distance_to

    # Used to find the next nearest location to truck
    def distance_from(self, origin):
        def distance_to(destination):
            return self.vertices.find(origin.identifier).distance_to_nearby(destination)

        return distance_to
