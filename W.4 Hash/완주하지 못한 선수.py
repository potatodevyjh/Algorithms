def solution(participant, completion):
    completion.sort()
    participant.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return  participant[-1]

'''
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
'''

participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
participant3 = ["mislav", "stanko", "mislav", "ana"]
completion3 = ["stanko", "ana", "mislav"]

print(solution(participant1, completion1))
print(solution(participant2, completion2))
print(solution(participant3, completion3))