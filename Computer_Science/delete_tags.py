def remove_tags(content):
    start_tag = content.find('<')
    while start_tag != -1:
        end_tag = content.find('>', start_tag)
        content = content[:start_tag] + " " + content[end_tag + 1:]
        start_tag = content.find('<')
    return content.split()

def remove_tags_second(content):
    start = content.find('<')
    if start != -1:
        end = content.find('>', start)
        content = content.replace(content[start:end + 1], ' ')
        return remove_tags_second(content)
    else:
        return content.split()



print(remove_tags('''<h1>Title</h1><p>This is a<a href="http://www.udacity.com">link</a>.<p>'''))
# >>> ['Title','This','is','a','link','.']
print(remove_tags_second('''<h1>Title</h1><p>This is a<a href="http://www.udacity.com">link</a>.<p>'''))


print(remove_tags('''<table cellpadding='3'><tr><td>Hello</td><td>World!</td></tr></table>'''))
# >>> ['Hello','World!']
print(remove_tags_second('''<table cellpadding='3'><tr><td>Hello</td><td>World!</td></tr></table>'''))


print(remove_tags("<hello><goodbye>"))
# >>> []

print(remove_tags("This is plain text."))
# >>> ['This', 'is', 'plain', 'text.']
print(remove_tags_second("This is plain text."))
