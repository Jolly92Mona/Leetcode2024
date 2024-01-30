from typing import List
'''Input: nums = [0,1,0,3,12]

Output: [1,3,12,0,0]'''

def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(0,len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left = left + 1
        print(nums)
moveZeroes([0,1,0,3,12])
