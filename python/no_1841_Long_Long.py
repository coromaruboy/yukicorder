import io
import sys

_INPUT = """\
5
"""
sys.stdin = io.StringIO(_INPUT)

count = int(input())
result = ""
for i in range(count):
    result += "Long"

print(result)