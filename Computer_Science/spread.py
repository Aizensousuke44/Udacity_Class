# n is the count of people who knew the news
# spread means one should let the count(spread) of people to know
# target means how many people knew the news
# how many time should spread
def count_spread(n, spread, target):
    if n >= target:
        return 0
    else:
        result = n + (n * spread)
        return count_spread(result, spread, target) + 1

print(count_spread(50000, 2, 150000)) # 1
print(count_spread(50000, 2, 150003)) # 2