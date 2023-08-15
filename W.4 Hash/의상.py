def solution(clothes):
    answer = 0
    cloth_dic = {}
    for i in range(len(clothes)):
        now = clothes[i][1]
        if now in cloth_dic:
            cloth_dic[now] += 1
        else:
            cloth_dic[now] = 1
    print(cloth_dic)
    cloth = list(cloth_dic.values())
    cloth_comb = cloth[0] + 1
    for j in range(1, len(cloth)):
        cloth_comb *= cloth[j] +1
    answer = cloth_comb - 1
    return answer

clothes1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes1))
print(solution(clothes2))