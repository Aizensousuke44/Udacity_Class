

def deep_reverse(p):
    result = []
    if isinstance(p, list):
        for i in range(len(p) - 1, -1, -1):
            result.append(deep_reverse(p[i]))
        return result
    else:
        return p

p = [1, [2, 3, [4, [5, 6]]]]
print(deep_reverse(p))
#
print(p)