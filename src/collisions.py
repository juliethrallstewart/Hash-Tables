import random
import statistics

def how_many_before_collisions(buckets, loops=1):
    
    """
    Roll random hashes into buckets (index) and print
    how many rolls before a hash collision
    """
    for i in range(loops):
        tries = 0
        tried = set()
        results = []
        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets

            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                break # because we have a collision
        result = tries / buckets * 100
        results.append(result)
        # print(f"{buckets} buckets, {tries} hashes before collision. ({tries / buckets * 100:.1f}%)")
        print(f"{buckets} buckets, {tries} hashes before collision. ({result:.1f}%)")

    print(f"Total average: {statistics.mean(results)}")
    print(tried)






how_many_before_collisions(32, 10)

# a set is a dictionary of only the keys