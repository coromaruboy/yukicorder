import io
import sys

_INPUT = """\
E
N
"""
sys.stdin = io.StringIO(_INPUT)

hougaku = {
    "N" : 1,
    "E" : 2,
    "S" : 3,
    "W" : 4
}

firstDirection = input()
lastDirection = input()
if hougaku[firstDirection] < hougaku[lastDirection]:
    print(hougaku[lastDirection] - hougaku[firstDirection])
elif hougaku[firstDirection] > hougaku[lastDirection]:
    print(4 - hougaku[firstDirection] + hougaku[lastDirection])
else:
    print(0)