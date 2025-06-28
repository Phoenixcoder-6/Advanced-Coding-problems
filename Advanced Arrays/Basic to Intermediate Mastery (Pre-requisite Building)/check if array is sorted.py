def check_sort(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

arr=[4,5,6,7,3]

if check_sort(arr):
    print("This array is sorted.")
else:
    print("This array is not sorted.")
    