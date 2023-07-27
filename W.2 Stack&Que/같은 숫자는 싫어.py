def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr [i-1]:
            answer.append(arr[i])
    return answer


def solution_2(arr): # 한 줄이라도 줄여보기
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer