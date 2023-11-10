import io
import sys

_INPUT = """\
2 1 2
"""
sys.stdin = io.StringIO(_INPUT)

fruits = sorted(list(map(int,input().split())))
bools = [False for i in range(4)]

for i in fruits:
    bools[i] = True
judge = bools.count(True)
if judge == 1:
    print(fruits[0])
elif judge == 2:
    if fruits[0] == fruits[1]:
        print(fruits[2])
    else:# ソートしてるから```fruits[0] == fruits[2]```は確認しなくてよい
        print(fruits[0])
else:
    print(bools.index(False))