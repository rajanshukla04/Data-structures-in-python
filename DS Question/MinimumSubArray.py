"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or 
equal to target. If there is no such subarray, return 0 instead.

"""
def minSubArrayLen(nums,target):
        left=0
        current_sum=0
        ans=1000000
        for right in range(len(nums)):
            current_sum=current_sum+nums[right]
            while current_sum>=target:
                ans=min(ans,right-left+1)
                current_sum-=nums[left]
                left+=1
        return 0 if ans==1000000 else ans 


target=7
nums=[2,3,1,2,4,3]
print("Length of subarray to find out the target value ",minSubArrayLen(nums,target))


        
