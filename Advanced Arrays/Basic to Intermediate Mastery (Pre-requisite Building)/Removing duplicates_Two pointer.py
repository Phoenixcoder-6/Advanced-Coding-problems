def twopointer(arr):
    arr.sort()
    p1=0
    p2=1

    while p2< len(arr):
        if arr[p1] == arr[p2]:
            arr.pop(p2)
        else:
            p1+=1
            p2+=1
    return arr

arr=[2,3,4,5,2]
res= twopointer(arr)
print(res)

