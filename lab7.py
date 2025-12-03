import time
import random 

# Hash Functions

def h0(key, ht_size):
    return 0

def h1(key, ht_size):
    return ord(key[0]) % ht_size

def h2(key, ht_size):
    x = 0
    for i in range(len(key)):
        ascii_code = ord(key[i])
        x = x + ascii_code
    return x % ht_size
    
def h3(key, ht_size):
    x = 0
    for i in range(len(key)):
        ascii_code = ord(key[i])
        x = 128 * x + ascii_code
    return x % ht_size

def h4(key, ht_size):
    prime = 31
    hash_value = 0
    for char in key:
        hash_value = (hash_value * prime + ord(char)) % ht_size
    return hash_value


# Hash Table Operations

def new_hash_table(size):
    ht = []
    for _ in range(size):
        ht.append([])
    return ht

def get_bucket(ht, key, hash_fun):
    if hash_fun == "h0":
        return ht[h0(key, len(ht))]
    elif hash_fun == "h1":
        return ht[h1(key, len(ht))]
    elif hash_fun == "h2":
        return ht[h2(key, len(ht))]
    elif hash_fun == "h3":
        return ht[h3(key, len(ht))]
    elif hash_fun == "h4":
        return ht[h4(key, len(ht))]
    else:
        raise ValueError(f"Unknown hash function: {hash_fun}")

def ht_insert(ht, key, hash_fun):
    bucket = get_bucket(ht, key, hash_fun)
    bucket.append(key)

def ht_search(ht, key, hash_fun):
    bucket = get_bucket(ht, key, hash_fun)
    for i in range(len(bucket)):
        if bucket[i] == key:
            return True
    return False


# Statistics Functions


def mean_bucket(ht):
    nonempty_buckets = 0
    entries = 0
    for bucket in ht:
        if len(bucket) > 0:
            nonempty_buckets = nonempty_buckets + 1
            entries = entries + len(bucket)
    if nonempty_buckets == 0:
        return 0
    return entries / nonempty_buckets

def largest_bucket(ht):
    max_so_far = 0
    for bucket in ht:
        if len(bucket) > max_so_far:
            max_so_far = len(bucket)    
    return max_so_far


# Benchmark Function


def run(hash_fun):
    hash_fun = str(hash_fun)
    
    # Validate hash function
    if hash_fun not in ["h0", "h1", "h2", "h3", "h4"]:
        print(f"Unknown hash function: {hash_fun}")
        return
    
    # Create a hash table with 100000 buckets
    size = 100000
    start_time = time.time()
    ht = new_hash_table(size)
    end_time = time.time()
    
    print("Created hash table with", size, "buckets in", (end_time-start_time), "seconds")
    
    # Generate random words
    words_Array = []
    for i in range(size):
        word = ""
        randomWordLength = random.randint(4,10)
        for j in range(randomWordLength):
            word = word + chr(random.randint(97,122))
        words_Array.append(word)

    assert size == len(words_Array)
    
    # Insert each word into the hash table
    insert_start = time.time()
    for words in words_Array:
        ht_insert(ht, words, hash_fun)
    insert_end = time.time()
       
    print("Inserted", len(words_Array), "words in", insert_end - insert_start, "seconds.")
        
    # Look up words
    lookup_start = time.time()
    for i in range(1000):
        random_word = words_Array[random.randint(0, len(words_Array)-1)]
        ht_search(ht, random_word, hash_fun)
    lookup_end = time.time()
    
    print("Searched for 1000 words in", (lookup_end-lookup_start), "seconds")
    
    print("\n--- Statistics for", hash_fun, "---")
    print("Number of entries in largest bucket:", largest_bucket(ht))
    print("Mean size of non-empty buckets:", mean_bucket(ht))
    print()

# Test Functions


def test_hash_functions():
    test_strings = ["Hash table", "Table hash", "Towers of Hanoi"]
    table_size = 100000
    
    print("Testing hash functions with table size 100000:")
    print("=" * 50)
    
    for s in test_strings:
        print(f"String: '{s}'")
        print(f"  h0: {h0(s, table_size)}")
        print(f"  h1: {h1(s, table_size)}")
        print(f"  h2: {h2(s, table_size)}")
        print(f"  h3: {h3(s, table_size)}")
        print(f"  h4: {h4(s, table_size)}")
        print()

def test_statistics():
    """Test the statistics functions"""
    test_ht = [["a", "b"], [], ["w", "x", "y", "z"], ["c"]]
    print("Testing statistics functions:")
    print("Hash table:", test_ht)
    print("Largest bucket:", largest_bucket(test_ht))
    print("Mean bucket size:", mean_bucket(test_ht))
    print()


# Main Execution


if __name__ == "__main__":
    # Test basic functionality
    test_hash_functions()
    test_statistics()
    
    # Run benchmarks for all hash functions
    print("Running performance benchmarks...")
    print("=" * 60)
    
    for hash_func in ["h0", "h1", "h2", "h3", "h4"]:
        run(hash_func)
        print("=" * 60)