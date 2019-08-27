from pyquery import PyQuery as pq

doc=pq(url='https://maoyan.com/board/4')
print(type(doc))
#print(doc.html())

print(doc('dd .name a').text())