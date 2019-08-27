import re

test_str = [
    'hello, every one!',
    'hello, peolpe',
    'hi, nice to meet you'
]

for t_str in test_str:
    result = re.match('^hello', t_str)
    print(t_str + '-->' + str(result))
