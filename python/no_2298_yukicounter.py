import io
import sys

_INPUT = """\
yukicoderyukicoderyukicoderyukicoderyukiyukicoderyukicoderyukicoder
"""
sys.stdin = io.StringIO(_INPUT)

input_string = input()

s = input_string.replace("yukicoder", "!")
ans = 0
n = 0
while n < len(s):
    x = 0
    while n < len(s) and s[n] == "!":
        n += 1
        x += 1
    ans = max(ans, x)
    n += 1
print(ans)
