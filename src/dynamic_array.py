class DynamicArray:
    def __init__(self, capacity=5):
        self.count = 0 # how much is currently used
        self.capacity = capacity # how much is currently allocated
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            #TODO resize
            print("Error, array is full")
            return
        
        for i in range(self.count, index, -1):#start at the end
            self.storage[i] = self.storage[i - 1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value):
        self.insert(0, value)

    def slice(self, beginning_index, end_index):
        #beginning and end

        #create subarray to store value

        #copy beginning to end to subarray

        #decide how this works.. what happend to the original array?
       
        #return value at the index
        pass

a = DynamicArray()
a.insert(0, 1)
a.append(2)# python 
for i in range(len(a.storage)):
    print(i)
# append
# insert

# pop([])
# slice = returns
# remove
# del = removed nothing 

# contains
# is not in
# is in

