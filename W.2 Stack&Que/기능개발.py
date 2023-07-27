def solution(progresses, speeds):
    answer = []
    day = 0
    cnt = 0 
    
    while progresses:
        if (progresses[0] + day * speeds[0]) >=100 :  # 하나의 기능 개발 완료 
            progresses.pop(0)
            speeds.pop(0)
            cnt +=1  # 넘어간 개발의 수 
            
        else : # 더 개발해야함 # 시간이 더 필요 
            if cnt > 0 : # 연속으로 넘어갈 기회를 놓침 
                answer.append(cnt) 
                cnt = 0
            day += 1
            
    answer.append(cnt)
    return answer



progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))