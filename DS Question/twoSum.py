"""
Given an array of integers and an integer target, return indices of the two 
numbers such that they add up to target.
"""


def twoSum(nums, target) :
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return [i,j]
        

arr=[2,7,11,15]
target=9

print('Target nums index in the array is ',twoSum(arr,target))

arr=[3,2,4]
target=6

print('Target nums index in the array is ',twoSum(arr,target))

