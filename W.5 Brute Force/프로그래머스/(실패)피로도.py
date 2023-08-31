def solution(k, dungeons):
    dungeons.sort()
    answer = -1
    for i in range(len(dungeons)):
        cnt = 0
        for j in range(len(dungeons) - i):
            if k >= dungeons[j][0]:
                k- dungeons[j][1]
                cnt += 1
        if answer < cnt:
            answer = cnt
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))