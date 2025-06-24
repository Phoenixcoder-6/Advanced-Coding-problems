def given_sum(arr,k):
    result=[]
    for i in range(len(arr)):
        for j in range(i+1 ,len(arr)):
            if arr[j] + arr[i] ==k:
                result.append([arr[i],arr[j]])

    return result


arr = [1, 2, 3, 4, 5]
k = 6
print("Pairs:", given_sum(arr, k))



