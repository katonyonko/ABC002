import io
import sys

_INPUT = """\
6
1 0 3 0 2 5
-1 -2 3 4 5 6
298 520 903 520 4 663
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  xa,ya,xb,yb,xc,yc=map(int,input().split())
  xb-=xa; yb-=ya; xc-=xa; yc-=ya
  print(abs(xb*yc-xc*yb)/2)