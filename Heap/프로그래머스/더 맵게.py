import sys
from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
        
    while scoville[0] < K:
        heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < K :
            answer = -1
    
    return answer