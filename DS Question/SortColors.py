"""
Given an array nums with n objects colored red, white, or blue, sort them 
in-place so that objects of the same color are adjacent, with the colors in 
the order red, white, and blue.

"""
# solution is just sort the  array

def Sort (nums):
     #using the bubble sort
        n=len(nums)
        for i in range(n):
            for j in range(n-1-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]


a=[0,1,1,2,0,0,2,1]
Sort(a) 
print(a)