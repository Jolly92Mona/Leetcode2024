
'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Input: nums = [3,3], target = 6
Output: [0,1]
'''

def twosum(nums,target):
    complement = 0
    for i in range(0,len(nums)):
        complement=target - nums[i]
        if complement in nums and nums.index(complement)!= i:
            return [i,nums.index(complement)]

result = twosum([3,3],6)
print(result)