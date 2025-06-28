def del_ele(arr,p):
    res= arr[:p] + arr[p+1:]
    return res

arr=[1,2,3,4,5,6]
p=3
res= del_ele(arr,p)
print(res)
