'''
딕셔너리 활용
'''

import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

arr = sorted(set(num))

dic = {arr[i]:i for i in range(len(arr))} # 딕셔너리 : 시간 복잡도 O(1)

for i in num:
    print(dic[i], end = " ")