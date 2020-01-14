# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.

        ie: 
        int index = hash_function(key) % array.length
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in
        #hash_table_storage(the array)  [hash_mod_key] = Value

        '''
        check = self.retrieve(key)
        print(check, "check line 98")

        if check == None: 

            hash = self._hash_mod(key)
            current = LinkedPair(key, value)

            

            if self.storage[hash] == None:
                self.storage[hash] = current
            else: 
            
                tail = self.storage[hash]
                while tail.next is not None:
                    tail = tail.next
                
                tail = tail.next
                tail = current
            
                current_storage = self.storage[hash]

                if current_storage.next is not None:
                    current_storage = current_storage.next

                current_storage.next = tail
        else:
                hash = self._hash_mod(key)
                current = self.storage[hash]
                while current is not None:
                    if current.key == key:
                        current.value = value
                        return current.value
                    else: 
                        current = current.next

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        check = self.retrieve(key)
        # print(check, "check line 103")

        if check == None: 
            return check
        else:
            hash = self._hash_mod(key)
            next_node = self.storage[hash].next
            prev = self.storage[hash]
            while prev is not None:
                
                if prev.key == key:
                    print(f"prev key: {prev.key}, Key: {key}")
                    prev.key = None
                   
                    return f"deleted key: {key}"
                elif next_node.key == key:
                    print(f"next node key: {next_node.key}, key: {key}")
                    prev.next = next_node.next
                    next_node = None
                    return f"deleted key: {key}"
                else:
                    next_node = next_node.next
                    prev = prev.next

    


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this i
        '''
        hash = self._hash_mod(key)
        current = self.storage[hash]
        while current is not None:
            if current.key == key:
                return current.value
            else: 
                current = current.next
        
        return None
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass




ht = HashTable(8)
ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")
print(ht.retrieve("key-4"))
print(ht.remove("key-7"))
print(ht.retrieve("key-7"))

# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
