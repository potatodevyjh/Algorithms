def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        new_array = []
        new_array = array[commands[a][0] - 1:commands[a][1]]
        new_array.sort()
        answer.append(new_array[commands[a][2] - 1])
    return answer