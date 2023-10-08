"""The next permutation of an array of integers is the next lexicographically 
greater permutation of its integer. Given an array of integers nums, find 
the next permutation of nums.

The replacement must be in place and use only constant extra memory
"""


def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        if length<=2:
            return nums.reverse()
        pointer =length-2
        while pointer>=0 and nums[pointer]>=nums[pointer+1]:
            pointer-=1
        if pointer ==-1:
            return nums.reverse()
        for x in range(length-1,pointer,-1):
            if nums[pointer]<nums[x]:
                nums[pointer],nums[x]=nums[x],nums[pointer]
                break
        nums[pointer+1:] = reversed(nums[pointer+1:])


# Creat
arr=[1,3,2]
nextPermutation(arr)
print("The next permutation of [1,3,2 ] is ",arr)

arr=[1,1,5]
nextPermutation(arr)
print("The next permutation of [1,1,5 ] is ",arr)
nextPermutation(arr)
print("The next permutation of [1,5,1 ] is ",arr)
nextPermutation(arr)
print("The next permutation of [5,1,1] is ",arr)
        