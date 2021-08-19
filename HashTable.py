# As per the requirements:
# Marshall Christian 001520145




# This table was inspired with the help of Cemel Tepe as well as Cemel Tepe - "Let's go hashing"
# Space complexity = O(n)
class HashTable(object):
    def __init__(self, size=10):
        self._struct = self.struct_creation(size)

    # insert() hashes the key. Then finds the modular
    # Then, uses the modular to find the appropriate bucket to append
    # Time complexity: O(n) - 'n' being the size of the bucket
    def insert(self, key, value):
        hashed_key = hash(key)
        bucket = self.find_bucket(hashed_key)

        mod = self.look_up_key_value_pair(hashed_key, bucket)

        if len(mod) == 0:
            bucket.append([hashed_key, value])
        else:
            mod[1] = value
        return True

    # remove() will find a key in the bucket and remove it.
    # Time complexity: O(1)
    def remove(self, key):
        bucket = self.find_bucket(key)
        if key in bucket:
            bucket.remove(key)

    # struck_creation() loops through the hash table and creates buckets for later
    # Time complexity: O(n)
    def struct_creation(self, size):
        struct = []
        for i in range(size):
            struct.append([])

        return struct

    # find() takes a key, hashes it and finds the matching bucket
    # Then, loops through the bucket to find the key-value pair
    # Time complexity: O(n) - 'n' being the size of the bucket
    def look_up(self, key):
        hashed_key = hash(key)
        bucket = self.find_bucket(hashed_key)

        key_value_pair = self.look_up_key_value_pair(hashed_key, bucket)

        if key_value_pair:
            return key_value_pair[1]

        raise Exception("Key-Value pair does not exist")

    # find_key_value_pair() loops through the bucket to find the needed key with value pair
    # Time complexity: O(n)
    def look_up_key_value_pair(self, key, bucket):
        for keey_value_pair in bucket:
            if keey_value_pair[0] == key:
                return keey_value_pair
        return []

    # find_bucket() uses hashed key to find the needed bucket
    # Time complexity: O(1)
    def find_bucket(self, key):
        return self._struct[key % len(self._struct)]

