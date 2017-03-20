import requests

def download_image():
    url = 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=175928787,2556338788&fm=23&gp=0.jpg'
    # Requests URL
    response = requests.get(url)
    print(response.status_code)

    with open('/home/mjhisoka/Udacity_Class/Python_base/demo.jpg', 'wb') as img:
        for chunk in response.iter_content(128):
            img.write(chunk)

    print(response.headers)


''' IMPROVED '''

def download_img_imp(url):
    from contextlib import closing
    with closing(requests.get(url, stream=True)) as resp:
        with open('/home/mjhisoka/Udacity_Class/Python_base/demo.jpg', 'wb') as img:
            for chunk in resp.iter_content(128):
                img.write(chunk)
    print(resp.headers)
    print(resp.status_code)


if __name__ == '__main__':
    url = 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=175928787,2556338788&fm=23&gp=0.jpg'

    download_img_imp(url)