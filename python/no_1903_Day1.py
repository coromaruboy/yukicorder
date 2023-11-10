import io
import sys

_INPUT = """\
2000
"""
sys.stdin = io.StringIO(_INPUT)

# 残問題数
questions = int(input())
dayCounter = 0

#if questions >= 7:
#    print((questions - 5)*7 -1)
#else:
#    print(questions)

while True:
    dayCounter += 1
    if dayCounter%7 == 0:
        questions += 6
    questions -= 1
    if questions == 0:
        break

print(dayCounter)