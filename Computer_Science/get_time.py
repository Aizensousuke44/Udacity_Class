from fabonacci import fabonacci, fabonacci_faster
import time

def time_execution(func):
    start = time.time()
    func
    used = time.time() - start

    return func, used

print(time_execution(fabonacci(30)))
print(time_execution(fabonacci_faster(100)))