import webbrowser
import time

def open_browsers(url, times):

    count = 0

    while count < times:
        print(time.ctime())
        time.sleep(5)
        webbrowser.open(url)
        count += 1


if __name__ == '__main__':
    open_browsers('https://github.com', 3)