# Declaring hashtable class
# Reference used: C950 Webinar 1 "Let's Go Hashing"
class Hashtable_Chaining:
    # constructor with initial capacity parameter set to 40
    def __init__(self, initial_capacity=40):
        # empty list
        self.table = []
        # For the length below 40, append an array to the table
        for i in range(initial_capacity):
            self.table.append([])


# function for inserting a new item into the table
    def insert(self, key, value):
        # Assign the bucket a key, which in this case will be a package ID (int)
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # Loop to check for if item exists, in which case perform an update instead of insert

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = value
                return True

            # If they key doesn't exist then append it to the end of the bucket_list
        key_value = [key, value]
        bucket_list.append(key_value)
        return True


# Method to search for a package with the specific search key, it will return the package if that key exists
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # search for the key in the list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
            return None


# Method for removing an item with the specified key
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # If the key exists, then remove the key and value
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

# Using the movie example for printing the hashtable
    def printHashtable(packageTable):
        for i in range(len(packageTable.table)+1):
            print("Package: {}".format(packageTable.search(i+1)))