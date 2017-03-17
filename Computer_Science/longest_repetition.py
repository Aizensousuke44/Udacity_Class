def longest_repetition(lst):
    if not lst:
        return None
    else:
        n = 0
        total = []
        count = 1
        lst.append(0)
        while n + 1 < len(lst):
            if lst[n] != lst[n + 1]:
                n = n + 1
                total.append(count)
                count = 1
            else:
                count = count + 1
                n = n + 1

        print (total)
        if len(set(total)) == 1:
            return lst[0]
        for i in total:
            if i > count:
                count = i
            else:
                continue

        tag = 0
        for i in total:
            if i != count:
               tag = tag + i
            else:
                break
        return lst[tag]


def longest_repetition(lst):
    best_element = None
    l_length = 0
    current = None
    current_length = 0
    for element in lst:
        if element != current:
            current = element
            current_length = 1
        else:
            current_length = current_length + 1
        if current_length > l_length:
            l_length = current_length
            best_element = current
    return best_element

print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print(longest_repetition([1, 2, 3, 4, 5]))
# 1

print(longest_repetition([]))
# None

print(longest_repetition([2, 2, 3, 3, 4, 4, 4]))