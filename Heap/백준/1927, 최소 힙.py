# 1927 최소 힙
import sys
import heapq

N = int(input())
heap = []

#Max Heap
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, x)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)


'''
9
0
12345678
1
2
0
0
0
0
32

시간 복잡도  :O(log2n)
'''