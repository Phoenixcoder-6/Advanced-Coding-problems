def longest_consequtive_elements(arr):
    arr_set=set(arr)
    longest=[]
    for num in arr_set:
        if num-1 not in arr_set:
            current=[]
            while num in arr_set:
                current.append(num)
                num+=1
            if len(current)> len(longest):
                longest=current
        
    return longest

arr=[1,4,200,3,499]
result= longest_consequtive_elements(arr)
print(result)