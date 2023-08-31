def solution(answers):
    person = []
    def answer(how, ans):
        cnt = 0
        how_ans = len(how)
        for i in range(len(ans)):
            if how[i % how_ans] == ans[i]:
                cnt += 1
        return cnt
    fst_how = [1, 2, 3, 4, 5]
    sec_how = [2, 1, 2, 3, 2, 4, 2, 5]
    thrd_how = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = []
    score.append(answer(fst_how, answers))
    score.append(answer(sec_how, answers))
    score.append(answer(thrd_how, answers))
    
    for idx, s in enumerate(score):
        if s == max(score):
            person.append(idx+1)
    
    print(score)
    return person

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))