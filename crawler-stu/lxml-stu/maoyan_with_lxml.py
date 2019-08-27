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


def print_one_page(url):
    html_str = get_one_page(url)
    html = etree.HTML(html_str)
    item_paimings = html.xpath('//dd/i/text()')
    item_imgs = html.xpath('//dd/a/img[@class="board-img"]/@data-src')
    str_title_params = '//dd/div[@class="board-item-main"]/div[@class="board-item-content"]/div[@class="movie-item-info"]'
    item_titles = html.xpath(str_title_params + '/p[@class="name"]/a/text()')
    item_starts = html.xpath(str_title_params + '/p[@class="star"]/text()')
    item_res_times = html.xpath(str_title_params + '/p[@class="releasetime"]/text()')
    str_item_score = '//dd/div[@class="board-item-main"]/div[@class="board-item-content"]/div[contains(@class,"movie-item-number")]/p'
    item_score_ints = html.xpath(str_item_score + '/i[@class="integer"]/text()')
    item_score_floats = html.xpath(str_item_score + '/i[@class="fraction"]/text()')
    print(item_imgs)

    moves = []
    for i in range(len(item_paimings)):
        move = {}
        move['index'] = item_paimings[i]
        move['img'] = item_imgs[i]
        move['title'] = item_titles[i]
        move['starts'] = item_starts[i].lstrip().rstrip()
        move['releaseTime'] = item_res_times[i]
        move['score'] = str(item_score_ints[i]).lstrip().rstrip() + str(item_score_floats[i]).lstrip().rstrip()
        moves.append(move)
    print(moves)


def main():
    for i in range(10):
        url = 'https://maoyan.com/board/4?offset=' + str(i * 10)
        print_one_page(url)


main()
