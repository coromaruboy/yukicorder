import io
import sys

_INPUT = """\
6
00123
00100
12345
00002
01001
10000
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
for _ in  range(n):
    print(int(input()))