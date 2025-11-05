def binarySearch(lst, target):
    left=0
    right=len(lst)-1
    while(left<=right):
        mid=left + (right - left) // 2
        if lst[mid]==target:
            return mid
        if target<lst[mid]:
            right=mid-1
        else:
            left=mid+1

lst=[1,2,3,4]
k=3
print(binarySearch(lst, k))
