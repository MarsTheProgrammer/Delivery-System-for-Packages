# As per the requirements:
# Marshall Christian 001520145

class HashTable(object):
    def __init__(self, size=10):
        self._struct = self.struct_creation(size)

    # insert() hashes the key. Then finds the modular
    # Then, uses the modular to find the appropriate bucket to append
    # Time complexity: O(n) - 'n' being the size of the bucket
    def insert(self, key, value):
        hashed_key = hash(key)
        bucket = self.find_bucket(hashed_key)

        extent = self.find_key_value_pair(hashed_key, bucket)

        if len(extent) == 0:
            bucket.append([hashed_key, value])
        else:
            extent[1] = value
        return True

    # find() takes a key, hashes it and finds the matching bucket
    # Then, loops through the bucket to find the key-value pair
    # Time complexity: O(n) - 'n' being the size of the bucket
    def find(self, key):
        hashed_key = hash(key)
        bucket = self.find_bucket(hashed_key)

        key_value_pair = self.find_key_value_pair(hashed_key, bucket)

        if key_value_pair:
            return key_value_pair[1]
        raise Exception("Key-Value pair does not exist")

    # struck_creation() loops through the hash table and creates buckets for later
    # Time complexity: O(n)
    def struct_creation(self, size):
        struct = []
        for i in range(size):
            struct.append([])

        return struct

    # find_bucket() uses hashed key to find the needed bucket
    # Time complexity: O(1)
    def find_bucket(self, key):
        return self._struct[key % len(self._struct)]

    # find_key_value_pair() loops through the bucket to find the needed key with value pair
    # Time complexity: O(n)
    def find_key_value_pair(self, key, bucket):
        for keey_value_pair in bucket:
            if keey_value_pair[0] == key:
                return keey_value_pair
        return []


