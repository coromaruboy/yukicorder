import io
import sys
import math

_INPUT = """\
5 3
"""
sys.stdin = io.StringIO(_INPUT)

x, y = map(int, input().split())

bitResult = x|y
print(math.factorial(bitResult))