def reverse_elements(arr,k):
    arr1= arr[:k]
    arr2= arr1[::-1]+ arr[-k+1:] 
    return arr2

arr=[1,2,3,4,5]
k=3
res= reverse_elements(arr,k)
print(res)