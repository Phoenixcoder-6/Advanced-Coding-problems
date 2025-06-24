#Version-1.0 time complexity: O(n)
'''
def prefix_sum(arr,L,R):
    res=0
    for i in range(L, R+1):
        res += arr[i]
    return res

arr=[2,3,4,5,6,7]
L=2
R=5
res1= prefix_sum(arr,L,R)
print("The result is:", res1)
'''
#Version- 2.0 ; Time complexity: O(1)

def prefix_Sum(arr):
    prefix= [0] * len(arr)
    prefix[0]= arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1]+arr[i]
    return prefix

def range_sum(prefix, L, R):
    if L==0:
        return prefix[R]
    else:
        return prefix[R] - prefix[L-1]
    
arr = [2, 3, 4, 5, 6, 7]
prefix1 = prefix_Sum(arr)

L = 2
R = 5
res = range_sum(prefix1, L, R)
print("The result is:", res)
        


    


