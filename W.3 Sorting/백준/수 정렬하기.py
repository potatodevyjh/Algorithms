N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
print(*arr, sep = '\n')



'''
5
5
2
3
4
1

1
2
3
4
5
'''