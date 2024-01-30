'''Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true'''

#hash set approach : time complexity : O(n) , space : O(n)
def contains_duplicate(nums):
    hashset=set()
    for item in nums:
        if item in hashset:
            return True
        else:
            hashset.add(item)
    return False


result = contains_duplicate([1,2,3,6])
print(result)