import re

test_str = 'aaabdffjeiofjkdvmdknfdsajfksldngkdsjgkjlsdjf';
result = re.findall('j.*?k', test_str)
for res_str in result:
    print(res_str)

# .匹配任意除换行符“\n”外的字符；
# *表示匹配前一个字符0次或无限次；
# +或*后跟?表示非贪婪匹配，即尽可能少的匹配，如*?重复任意次，但尽可能少重复；
# .*?表示匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复。
# a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab和ab。
