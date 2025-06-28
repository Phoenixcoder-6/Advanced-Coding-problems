def second_largest(arr):
    arr.sort()
    return arr[-2]

arr=[9,7,2,3,5]
res= second_largest(arr)
print(res)