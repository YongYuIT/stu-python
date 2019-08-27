import re

test_str = [
    'abcdabcd',
    'abcddddd',
    'dddddddd'
]

for t_str in test_str:
    result = re.match("abcd*", t_str)
    print(t_str + '-->' + str(result))
print('---------------------------------------')
for t_str in test_str:
    result = re.match("(abcd)*", t_str)
    print(t_str + '-->' + str(result))
print('---------------------------------------')
for t_str in test_str:
    result = re.match("abcd{2}", t_str)
    print(t_str + '-->' + str(result))
print('---------------------------------------')
for t_str in test_str:
    result = re.match("(abcd){2}", t_str)
    print(t_str + '-->' + str(result))
