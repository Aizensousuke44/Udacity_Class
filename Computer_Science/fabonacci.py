def fabonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fabonacci(num - 1) + fabonacci(num - 2)

def fabonacci_faster(num):
    current, after = 0, 1
    for _ in range(num):
        current, after = after, current + after
    return current

if __name__ == '__main__':
    print(fabonacci(20))