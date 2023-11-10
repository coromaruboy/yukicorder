import io
import sys

_INPUT = """\
#.#
#.#
.#.
"""
sys.stdin = io.StringIO(_INPUT)

result = True
v1 = ""
v2 = ""
v3 = ""

for i in range(3):
    h = list(input())
    if h[0] != h[2]:
        result = False
    if h[0] == h[1] or h[1] == h[2]:
        result = False
    if i != 0:
        if v1 == h[0] or v2 == h[1] or v3 == h[2]:
            result = False
    v1 = h[0]
    v2 = h[1]
    v3 = h[2]

if result:
    print("Yes")
else:
    print("No")
