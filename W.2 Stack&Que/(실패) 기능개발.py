'''
실패 이유 : 모든 풀이과정을 리스트에 넣어서 저장하려고 했어서
'''
def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range (1, len(progresses)):
        progresses[i] = 100 - progresses[i]
        day_q = progresses[i] // speeds[i]
        day_r = progresses[i] % speeds[i]
        if i == 0:
            if day_r == 0:
                days.append(day_q)
            else:
                days.append(day_q + 1)
        else:
            if day_q > days[i]:
                if day_r == 0:
                    days.append(day_q)
                else:
                    days.append(day_q + 1)
    
    days.sort()
    answer.append(days[0])
    for j in range(1, len(days)):
        answer.append(days[j] - days[j-1])
        
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))