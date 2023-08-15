def solution(citations):
    answer = 0
    citations.sort()
    total = len(citations)

    for i in range(total):
        print(citations[i])
        if citations[i] >= total-i:
            answer = total-i
            return answer
    return answer

citations = [3, 0, 6, 1, 5]	
print(solution(citations))