import io
import sys

_INPUT = """\
5 3
"""
sys.stdin = io.StringIO(_INPUT)

number, count = map(int, input().split())
choise = 10**7

print(choise)
print(pow(number,count,choise))