def left_rotate(arr):
    rotate=arr[1:] + arr[:1]
    return rotate


arr=[1,2,3,4,5]
res= left_rotate(arr)
print(res)