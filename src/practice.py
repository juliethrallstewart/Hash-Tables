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
        current = LinkedPair(hash, value)
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
            print(hash)
            print(tail.next, "this is tail next 111")
            print(tail.value, "tail value line 113")
            print(tail.key, "tail key line 113")

            # current_next = self.storage[hash]
            # if current_next.next == None:
            #     current_next.next = current
            # else:
            #     current_next.next

        #         def insert_after(self, value):
        #     current_next = self.next
        # self.next = ListNode(value, self, current_next)
        # if current_next:
        #     current_next.prev = self.next
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this i
        '''
        hash = self._hash_mod(key)
        if self.storage[hash]:
            return self.storage[hash].value
       
 
   

       


        

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
        print(f"{i.key}, {i.value}")

print(h.retrieve("item_2"), "retrieved item")

# while h.storage[4].next is not None:
    
#     print(f"value h.storage[4]: {h.storage[4].value}")

# lp = LinkedPair("tst", 1)
# lp.next = LinkedPair('bob', 2)
# lp.next.next = LinkedPair('sue', 3)

# current = lp
# while current.next is not None:
#     print(current.value)
#     current = current.next