def quote_text(url):

    with open(url) as quote:
        content = quote.read()
        print(content)

if __name__ == '__main__':
    url = '/home/mjhisoka/Udacity_Class/README.md'

    quote_text(url)