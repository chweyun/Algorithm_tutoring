from heapq import *
input = __import__('sys').stdin.readline
n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)])
hq = []
for i in range(n):
    if hq and hq[0] <= arr[i][0]: heappop(hq)
    heappush(hq, arr[i][1])
print(len(hq))
