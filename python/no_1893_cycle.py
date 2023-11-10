import io
import sys

_INPUT = """\
0 4
"""
sys.stdin = io.StringIO(_INPUT)

zahyo = list(map(int, input().split()))

zahyo.sort()

if zahyo[0] + 4 != zahyo[1]:
    print(zahyo[0] + 4)
else:
    if zahyo[0] + 8 == 12:
        print(0)
    elif zahyo[0] + 8 > 12:
        print(zahyo[0] - 4)
    else:
        print(zahyo[0] + 8)