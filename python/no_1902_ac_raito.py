import io
import sys

_INPUT = """\
10/3456
"""
sys.stdin = io.StringIO(_INPUT)

n1, n2 = map(int, input().split('/'))
print(round((n1/n2), 5))