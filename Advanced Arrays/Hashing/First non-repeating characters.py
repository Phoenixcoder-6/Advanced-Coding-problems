def first_unique_char(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return -1


s="abcad"
res= first_unique_char(s)
print("First Non-repeating charecter is:", res)