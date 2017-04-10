
data1 = [1, 2, 5, 10, -20, 2, 5, 7, 5, 1]

def mode(data):
    flag = 0
    for i in range(len(data)):
        icount = data.count(data[i])
        if icount > flag:
            flag = icount
            mode_value = data[i]
    return mode_value

print(mode(data1))
