def solution(nums):
    n_dict = dict()
    
    for n in nums:
        n_dict[n] = 1 
        
    if len(nums) // 2 <= len(n_dict):
        return len(nums) // 2 
    
    return len(n_dict)


'''
def solution(nums):
    # 최솟값( 전체 종류/2, 중복 제거 종류/2 )
    return min(len(nums)/2, len(set(nums)))
'''

nums1 = [3,1,2,3]
nums2 = [3,3,3,2,2,4]
nums3 = [3,3,3,2,2,2]

print("#1")
print(solution(nums1))
print("#2")
print(solution(nums2))
print("#3")
print(solution(nums3))