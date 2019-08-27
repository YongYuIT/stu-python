import re

test_str = [
    'America country',
    'Chinese people',
    'Canada goods',
    'England food'
]

for t_str in test_str:
    result = re.match('^[CE]', t_str)
    print(t_str + '-->' + str(result))

print('---------------------------------------')

for t_str in test_str:
    result = re.match('^[^CE]', t_str)
    print(t_str + '-->' + str(result))
