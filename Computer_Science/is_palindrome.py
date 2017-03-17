def is_palindrome(content):
    if isinstance(content, int):
        content = str(content)
    if len(content) <2:
        return True
    if content == content[::-1]:
        return True
    else:
        return False

def is_palindrome_another(content):
    if isinstance(content, int):
        content = str(content)
    if len(content) <2:
        return True
    if content[0] == content[-1]:
        return is_palindrome_another(content[1:-1])
    else:
        return False

def is_palindrome_another_(content):
    if isinstance(content, int):
        content = str(content)
    if len(content) <2:
        return True
    for i in range(len(content) // 2):
        if content[i] != content[-(i + 1)]:
            return False
    return True

print(is_palindrome_another(345676543))
print(is_palindrome(345676543))
print(is_palindrome_another_(345676543))