def solution(participant, completion):
    answer = ''
    for comp in completion:
        for parti in participant:
            if comp == parti:
                participant.remove(comp)
                break
            #print(comp, parti)
            answer = participant[0]
                
    return answer

    
participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
participant3 = ["mislav", "stanko", "mislav", "ana"]
completion3 = ["stanko", "ana", "mislav"]

print(solution(participant1, completion1))
print(solution(participant2, completion2))
print(solution(participant3, completion3))