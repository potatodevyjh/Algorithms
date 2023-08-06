arr = []
mean = 0
for i in range(5):
    arr.append(int(input()))
    mean += arr[i]
arr.sort()
mean = mean // 5

print(mean, arr[2], sep = '\n')