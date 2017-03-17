
def bucket_find(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None


def hash_string(s, size):
    h = 0
    for c in s:
        h += ord(c)
    return h % size

def hashtable_lookup(htable, key):
    entry = bucket_find(hashtable_get_bucket(htable, key), key)
    if entry:
        return entry[1]
    else:
        return None

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]


def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])

def make_hashtable(size):
    table = []
    for _ in range(size):
        table.append([])
    return table

table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'Mysql', 'Liskov')
hashtable_update(table, 'ML', 'Eich')

print(hashtable_lookup(table, "Python"))
print(table)

# Monty
# [[], [], [['Python', 'Monty']], [['ML', 'Eich']], [['Mysql', 'Liskov']], [], [], [], [], []]
