from pyquery import PyQuery as pq


def print_one_page(page_url):
    doc = pq(url=page_url)
    dds = doc.find('dd')
    indexs = dds.children('.board-index').items()
    imgs = dds.find('.board-img').items()
    dd_infos = dds.find('.movie-item-info')
    titles = dd_infos.find('.name a').items()
    starts = dd_infos.find('.star').items()
    release_times = dd_infos.find('.releasetime').items()
    info_scores = dd_infos.parent().find('.movie-item-number.score-num')
    scores_ints = info_scores.find('.integer').items()
    scores_floats = info_scores.find('.fraction').items()

    moves = []
    while True:
        try:
            move = {}
            move['index'] = next(indexs).text()
            move['img'] = next(imgs).attr('data-src')
            move['title'] = next(titles).text()
            move['starts'] = next(starts).text().lstrip().rstrip()
            move['releaseTime'] = next(release_times).text()
            move['score'] = str(next(scores_ints).text()).lstrip().rstrip() + str(
                next(scores_floats).text()).lstrip().rstrip()
            moves.append(move)
        except StopIteration:
            break
    print(moves)


def main():
    for i in range(10):
        url = 'https://maoyan.com/board/4?offset=' + str(i * 10)
        print_one_page(url)


main()
