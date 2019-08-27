import re

test_str = [
    'hello, yong',
    'good job, yong',
    "what's your problem?"
]

for t_str in test_str:
    result = re.match('.*yong$', t_str) #点表示匹配除换行外任意字符，*表示重复任意次，.*结合就时匹配任意长度字符串
    print(t_str + '-->' + str(result))
