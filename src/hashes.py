
#hashes
#it doesnt matter how many characters we type of if we 
# use spaces or don't the hash will always be the same length

import time
import hashlib

n = 1000000
key  = b"STR"

#python has a built in hash function = python3

for _ in range(10):
    print(hash(key)) #changes every time instantiated 
    #based off a seed

for _ in range(10): #returns the same hash every time
    print(hashlib.sha256(key).hexdigest())

for _ in range(10): #returns the same hash every time
    print(int((hashlib.sha256(key).hexdigest(), 16) % 8))


#the way that a hash table works, we have keys:

# flavor  hash (flavor hashes out) and we can store vanilla
# color           (color hashes out) and we can store blue
# type
# size
# amount
# etc

# https://www.geeksforgeeks.org/bitwise-operators-in-c-cpp/