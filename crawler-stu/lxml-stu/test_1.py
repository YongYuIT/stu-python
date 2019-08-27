import requests
from lxml import etree


def get_one_page(url):
    heads = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    reponse = requests.get(url, headers=heads)
    if reponse.status_code == 200:
        return reponse.text
    return None


html_str = get_one_page('https://maoyan.com/board/4')
html = etree.HTML(html_str)
all_elms = html.xpath('//*')
for elm in all_elms:
    print(elm)
print('-----------------------------------')
dds = html.xpath('//dd')
for elm in dds:
    print(elm)
print('-----------------------------------')
dd_is = html.xpath('//dd/i')
for elm in dd_is:
    print(elm)
