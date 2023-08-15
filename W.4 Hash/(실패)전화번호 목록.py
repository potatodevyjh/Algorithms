def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book) - i - 1):
            length = len(phone_book[i])
            now = i + j + 1
            if length <= len(phone_book[now]):
                now_phone = phone_book[now][:length]
                if phone_book[i] == now_phone:
                    answer = False
                    break
    return answer


phone_book1 = ["119", "97674223", "1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = ["12","123","1235","567","88"]

print(solution(phone_book1))
print(solution(phone_book2))
print(solution(phone_book3))