import sys
from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    print(scoville)
        
    while scoville[0] < K:
        heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
        print(scoville)
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
    
    return answer


scoville = list(map(int, input().split()))
K = int(input())
print(scoville)
solution(scoville, K)

'''
1 2 3 9 10 12
7
'''