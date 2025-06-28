def insert(arr,p,n):
    arr1= arr[:p]+ [n]+ arr[p:]
    return arr1

arr=[1,2,4,5,6,7]
p=2
n=3
res=insert(arr,p,n)
print("New updated array:",res)