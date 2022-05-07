import io
import sys

_INPUT = """\
6
10 11
100000000 10000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  print(max(map(int,input().split())))