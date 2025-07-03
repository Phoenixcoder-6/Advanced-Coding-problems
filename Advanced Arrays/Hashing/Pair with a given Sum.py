def pair_sum(arr,k):
    res=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == k:
                res.append((arr[i],arr[j])) 
                return res         
    return False


arr=[2,3,4,5,10]
k=14
res= pair_sum(arr,k)
print(res)