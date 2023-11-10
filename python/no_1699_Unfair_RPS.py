import io
import sys

_INPUT = """\
1 2
"""
sys.stdin = io.StringIO(_INPUT)

b, c = input().split()

if b == c:
    print("Yes")
else:
    print("No")