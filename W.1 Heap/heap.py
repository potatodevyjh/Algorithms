from heapq import heappush, heappop, heapify
heap = []

print("#1 힙에 원소 추가")
heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 7)
heappush(heap, 3)
print(heap)
print("시간 복잡도 : 0(log(n))" + "\n")

print("#2 힙에 원소 삭제")
print(heappop(heap))
print(heap)
print("시간 복잡도 : 0(log(n))" + "\n")

print("#3 최솟값 삭제하지 않고 얻기")
print(heap[0])
print("시간 복잡도 : ?" + "\n")


print("#4 기존 리스트를 힙으로 변환")
nums = [4, 1, 7, 3, 8, 5]

heap = nums[:]
heapify(heap)

print(nums)
print(heap)
print("시간 복잡도 : ?" + "\n")

print("#5 최대 힙")
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
    print(heappop(heap)[1])  # index 1
print("시간 복잡도 : ?" + "\n")


print("#6 n번째 최소값/최대값")
def nth_smallest(nums, n):
    heap = []
    for num in nums:
        heappush(heap, num)

    nth_min = None
    for _ in range(n):
        nth_min = heappop(heap)

    return nth_min

def nth_smallest_2nd(nums, n):
    heapify(nums)

    nth_min = None
    for _ in range(n):
        nth_min = heappop(nums)

    return nth_min

print(nth_smallest([4, 1, 7, 3, 8, 5], 3))
print("시간 복잡도 : ?" + "\n")


print("#7 힙 정렬")
def heap_sort(nums):
    heap = []
    for num in nums:
        heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heappop(heap))
        return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))
print("시간 복잡도 : ?" + "\n")