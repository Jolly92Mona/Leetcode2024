'''
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
Example 1:
Input: nums = [3,0,1]
Output: 2
'''

def missingNumber(nums):
    total = 0
    for i in range(0,len(nums)+1):
        total = total + i
    return total - sum(nums)

nums = [3,0,1]
result = missingNumber(nums)
print(result)

