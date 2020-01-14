# class HashTable:
#     '''
#     A hash table that with `capacity` buckets
#     that accepts string keys
#     '''
#     def __init__(self, capacity):
#         self.capacity = capacity  # Number of buckets in the hash table
#         self.storage = [None] * capacity


#     def _hash(self, key):
#         '''
#         Hash an arbitrary key and return an integer.

#         You may replace the Python hash with DJB2 as a stretch goal.
#         '''
#         return hash(key)

#     def _hash_mod(self, key):
#         '''
#         Take an arbitrary key and return a valid integer index
#         within the storage capacity of the hash table.
#         '''
#         return self._hash(key) % self.capacity

#     def insert(self, key, value):
#         '''
#         Store the value with the given key.

#         Hash collisions should be handled with Linked List Chaining.

#         Fill this in.

#         #hash_table_storage(the array)  [hash_mod_key] = Value

        

#         '''
#         hash = self._hash_mod(key)
#         if self.storage[hash] == None:
#             self.storage[hash] = value
#         else: 

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
                
            
       
 
   

       


        

h = HashTable(5)
# print(h._hash("STR"))
# print(h._hash_mod("STR"))
h.insert("item_1", 1)
h.insert("item_2", 2)
h.insert("item_3", 3)
h.insert("item_4", 4)
h.insert("item_5", 5)
# print(h.storage, "this is the storage")
# print(h.storage[2].key, "this is the value")

# lp = LinkedPair("tst", 1)
# print(lp.key)
for i in h.storage:
    if i is not None:
        print(f"{i.key}, {i.value}, {i.next}")

print(h.retrieve("item_1"), "retrieved item 1")
print(h.retrieve("item_2"), "retrieved item 2")
print(h.retrieve("item_3"), "retrieved item 3")
print(h.retrieve("item_4"), "retrieved item 4")
print(h.retrieve("item_5"), "retrieved item 5")


# lp = LinkedPair("tst", 1)
# lp.next = LinkedPair('bob', 2)
# lp.next.next = LinkedPair('sue', 3)

# current = lp
# while current.next is not None:
#     print(current.value)
#     current = current.next
ht = HashTable(2)

ht.insert("line_1", "Tiny hash table")
ht.insert("line_2", "Filled beyond capacity")
ht.insert("line_3", "Linked list saves the day!")
print(ht.retrieve("line_1"))
print(ht.retrieve("line_2"))
print(ht.retrieve("line_3"))