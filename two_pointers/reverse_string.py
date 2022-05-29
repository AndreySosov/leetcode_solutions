def reverseString(s):
    k = len(s)-1
    i = 0
    cou = 0
    while i <= k:
        temp = s.pop()
        s.insert(cou,temp)
        cou += 1
        i += 1
def reverseString(s):
    new = s[:] = s[::-1]
    return new
st = ["h","e","l","l","o","m","y","f","r","i","e","n","d"]
st1 = ["h","e","l","l"]

print(reverseString(st1))
