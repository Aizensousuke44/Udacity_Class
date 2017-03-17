def hashtable_update(htable, key, value):

    target = hashtable_get_bucket(htable, key)
    # if target == []:
    #     hashtable_add(htable, key, value)
    for item in target:
        if key == item[0]:
            item[1] = value
            return htable
    target.append([key, value])

def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None


def hashtable_add(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key, value])


def hashtable_get_bucket(htable, keyword):
    return htable[hash_string(keyword, len(htable))]


def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out


def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table


table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
         [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
hashtable_update(table, 'Luke', 7)
print (table)