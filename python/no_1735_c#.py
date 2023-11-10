import io
import sys

_INPUT = """\
E
"""
sys.stdin = io.StringIO(_INPUT)

sound = input()

if sound == 'E':
    print('F')
elif sound == 'B':
    print('C')
else:
    print(sound + '#')