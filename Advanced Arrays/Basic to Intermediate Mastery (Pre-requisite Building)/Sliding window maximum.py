from collections import deque
def maxslidingwindow(nums,k):
    q= deque()
    result= []

    for i in range(len(nums)):
        while q and q[0] <= i-k :
            q.popleft()

        while q and nums[q[-1]] < nums[i]:
            q.pop() 
        q.append(i)
        if i >=k-1:
            result.append(nums[q[0]])
    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
res= maxslidingwindow(nums,k)
print(res)