def anagram(w1,w2):
    w1= w1.lower()
    w2= w2.lower()
    if len(w1) != len(w2):
        return False
    freq={}
    for ch in w1:
        freq[ch]= freq.get(ch,0)+1

    for ch in w2:
        if ch not in freq:
            return False
        freq[ch]-=1
        if freq[ch]<0:
            return False
    return True    

w1="Silent"
w2="Listen"
res= anagram(w1,w2)
if res ==True:
    print("The strings are anagram")
else:
    print("The strings are not anagram")



    