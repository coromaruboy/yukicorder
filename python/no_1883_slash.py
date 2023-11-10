import io
import sys

_INPUT = """\
123456
"""
sys.stdin = io.StringIO(_INPUT)

l = [int(x) for x in list(str(input()))]

print(max(l) - min(l))
