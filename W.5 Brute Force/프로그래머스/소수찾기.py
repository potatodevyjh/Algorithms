from itertools import permutations

def solution(numbers):
    num = {}
    answer = 0
    per = []
    nums = []
    '''
    for i in range(len(numbers)):
    if num.get(numbers[i]) == None:
        num[numbers[i]] = 1
    else:
        num[numbers[i]] += 1
    '''

    def prime_num(number):
        a = 0
        if number >= 2:
            for i in range(1, number):
                print(i)
                if number % i == 0:
                    break
                return number

    for i in range(1, len(numbers)+1) :
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
        #print(nums)
    per = list(set(map(int, set(sum(nums, [])))))
    print(per)
    for idx, s in enumerate(per):
        if prime_num(s) == s:
            answer += 1
            print("here", s, answer)
    return answer


print(solution("17"))
print(solution("011"))