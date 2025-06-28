def left_rotate(arr,d):
    rotate= arr[d:]+arr[:d]
    return rotate

arr=[3,4,6,7,8]
d=3
res= left_rotate(arr,d)
print(res)