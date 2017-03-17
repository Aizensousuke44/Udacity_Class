def make_next_row(row):
    result = []
    prev = 0
    for i in row:
        result.append(i + prev)
        prev = i
    result.append(prev)
    return result

def triangle(n):
    result = []
    current = [1]
    for _ in range(n):
        result.append(current)
        current = make_next_row(current)
    return result

for i in triangle(4):
    print(i)

###########################################

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


# triangles is a generator
# print triangles with for statement
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

''' From http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000'''
