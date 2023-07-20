# 11279 최대 힙
import sys
import heapq

N = int(sys.stdin.readline())   # 총 연산의 개수
heap_list = []  # 최대 힙으로 사용할 힙 선언

for _ in range(N):
    x = int(sys.stdin.readline())   
    
    if x != 0:  # 입력 받은 수가 0이 아닌 자연수 라면
        # 힙에 추가. 단, 최대힙으로 작동되도록 - 부호 붙여서
        heapq.heappush(heap_list, -x) 
        
    else:
        if len(heap_list) == 0: # 배열이 비어 있으면
            print(0)    # 0을 출력
        else:   # 배열이 비어 있지 않으면, heap에서 가장 큰 값을 꺼내서 출력, 배열에서 제거
            # 최대힙이 되도록 - 부호를 다시 붙여서 추가
            result = heapq.heappop(heap_list)
            print(-result)
        

'''
13
0
1
2
0
0
3
2
1
0
0
0
0
0
'''

