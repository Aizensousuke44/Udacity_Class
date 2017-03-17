def make_converter(match, replace_):
    return [match, replace_]


def apply_converter(l, string):
    prev = None
    while prev != string:
        prev = string
        position = string.find(l[0])
        if position != -1:
            string = string[:position] + l[1] + string[position + len(l[0]):]
    return string

c = make_converter('aa', 'a')
print(apply_converter(c, 'aaaa'))
# a