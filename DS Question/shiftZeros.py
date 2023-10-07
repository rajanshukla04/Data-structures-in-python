"""Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

"""
arr=[1, 2, 0, 4, 3, 0, 5, 0]
j=0
while 0 in arr:
    arr.remove(0)
    j+=1
while j>0:
    arr.append(0)
    j-=1
print(arr)
"""


#2nd Apporach 

def shiftZeros(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print(shiftZeros(arr))




