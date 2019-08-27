import re

test_str = 'aaabdffjeiiofjkdvmdknfdsajfksldngkdsjgkjlsdjf';

result = re.findall('f.*?(i+).*?(fj)*?k', test_str)
print(result)
