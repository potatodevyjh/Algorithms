import copy  

def solution(sizes):
    wallet = copy.deepcopy(sizes)
    for i in range (len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            wallet[i][0] = sizes[i][1]
            wallet[i][1] = sizes[i][0]
    print(wallet)
    max_0 = wallet[0][0]
    max_1 = wallet[0][1]
    for j in range(len(sizes) - 1):
        if max_0 < wallet [j + 1][0]:
            max_0 = wallet[j + 1][0]
        if max_1 < wallet [j + 1][1]:
            max_1 = wallet[j+1][1]
        print(max_0, max_1)
            
    answer = max_0 * max_1
    return answer


sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution(sizes1))
print(solution(sizes2))
print(solution(sizes3))