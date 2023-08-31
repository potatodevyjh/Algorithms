def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            garo = int(yellow/i)
            sero = i
            if brown == (garo+sero) *2 + 4:
                answer.append(garo+2)
                answer.append(sero+2)
                break
    
    return answer

brown1 = 10
yellow1 = 2

brown2 = 8
yellow2 = 1

brown3 = 24
yellow3 = 24

print(solution(brown1, yellow1))
print(solution(brown2, yellow2))
print(solution(brown3, yellow3))
