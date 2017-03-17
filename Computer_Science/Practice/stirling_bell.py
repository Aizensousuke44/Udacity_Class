# The formula for calculating the Stirling numbers is

#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

# Furthermore, the Bell number B(n) is the number of ways of splitting n
# into any number of parts, that is,

# B(n) is the sum of S(n,k) for k =1,2, ... , n.

# Write two procedures, stirling and bell. The first procedure, stirling
# takes as its inputs two positive integers of which the first is the
# number of items and the second is the number of sets into which those
# items will be split. The second procedure, bell, takes as input a
# positive integer n and returns the Bell number B(n).

def stirling(total, num):
    if total == num or num == 1:
        return 1
    if total < num:
        return 0
    else:
        return num * stirling(total - 1, num) + stirling(total - 1, num - 1)


def bell(num):
    count = 0
    for total in range(1, num + 1):
        count = count + stirling(num, total)
    return count

print(stirling(1, 1))
# >>> 1
print(stirling(2, 1))
# >>> 1
print(stirling(2, 2))
# >>> 1
print(stirling(2, 3))
# >>>0

print(stirling(3, 1))
# >>> 1
print(stirling(3, 2))
# >>> 3
print(stirling(3, 3))
# >>> 1

print(stirling(4, 1))
# >>> 1
print(stirling(4, 2))
# >>> 7
print(stirling(4, 3))
# >>> 6
print(stirling(4, 4))
# >>> 1

print(stirling(5, 1))
# >>> 1
print(stirling(5, 2))
# >>> 15
print(stirling(5, 3))
# >>> 25
print(stirling(5, 4))
# >>> 10
print(stirling(5, 5))
# >>> 1

print(stirling(20, 15))
# >>> 452329200

print(bell(1))
# >>> 1
print(bell(2))
# >>> 2
print(bell(3))
# >>> 5
print(bell(4))
# >>> 15
print(bell(5))
# >>> 52
print(bell(15))
# >>> 1382958545