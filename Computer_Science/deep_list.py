def deep_count(l):
    sum = 0
    for i in l:
        sum += 1
        if isinstance(i, list):
            sum += deep_count(i)
    return sum

print(deep_count([1, [2, 3], 4]))