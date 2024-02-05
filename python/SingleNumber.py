'''Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
'''

#using bit manipulation (XOR)

def singleNumber(nums):
    result = 0
    for i in nums:
        result = result ^ i
    return result

nums = [1,5,2,1,2]
output = singleNumber(nums)
#print(output)

#Using hashset()

def SingleNumber2(nums):
    newList = []
    s = sorted(nums)
    for i in s:
        if i not in newList:
            newList.append(i)
        else:
            newList.pop()
    return newList[0]


res = SingleNumber2(nums)
print(res)