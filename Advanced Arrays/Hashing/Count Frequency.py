def countfreq(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

arr=[1,2,3,2,3,1,3,4,5]
res= countfreq(arr)
print(res)
