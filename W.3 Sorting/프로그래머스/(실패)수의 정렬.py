'''
실패 이유 : 너무 오래 걸림
'''
def solution(numbers):
    answer = ''
    num = []
    new_num = []
    for i in range(len(numbers)):
        new_num.append(str(numbers[i])[0])
        num.append(i)
    print(new_num)
    dic = dict(zip(num, new_num))
    dic = dict(sorted(dic.items(), reverse=True,  key = lambda item: item[1]))
    print(dic)

    for key in dic.keys():
        answer += str(numbers[key])
    return answer

numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]	
print(solution(numbers2))