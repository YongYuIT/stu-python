import requests
import re


def get_one_page(url):
    heads = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    reponse = requests.get(url, headers=heads)
    if reponse.status_code == 200:
        return reponse.text
    return None


def print_one_page(url):
    html_str = get_one_page(url)
    pat = re.compile(
        '<dd>.*?board-index-\d.*?".*?>(.*?)</.*?title.*?="(.*?)".*?data-src.*?=.*?"(.*?)".*?star.*?".*?>(.*?)</.*?releasetime.*?".*?>(.*?)</.*?integer.*?".*?>(.*?)</.*?fraction.*?".*?>(.*?)</.*?</dd>',
        re.S)
    resluts = re.findall(pat, html_str)
    for dd_strs in resluts:
        for dd_atr in dd_strs:
            print(str(dd_atr).lstrip().rstrip())
        print("----------------------------------------")


def main():
    for i in range(10):
        url = 'https://maoyan.com/board/4?offset=' + str(i * 10)
        print_one_page(url)


main()
