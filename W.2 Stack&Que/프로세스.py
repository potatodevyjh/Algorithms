from collections import deque

def solution(priorities, location):
    answer = []
    queue = deque((idx, j) for idx, j in enumerate(priorities))
    while queue:
        process = queue.popleft()
        # 우선순위가 더 높은 프로세스가 하나라도 있으면 큐에 다시 추가
        if queue and any(process[1] < q[1] for q in queue):
            queue.append(process)
        else:
            answer.append(process)
    
    # location 실행 순서 찾기
    for i in answer:
        if i[0] == location:
            return answer.index(i)+1
            
priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))