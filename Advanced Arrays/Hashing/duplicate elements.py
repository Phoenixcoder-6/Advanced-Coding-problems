def duplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)

arr="ankita"
res= duplicate(arr)
if res==True:
    print("Duplicate present.")
else:
    print("No duplicate is present.")
