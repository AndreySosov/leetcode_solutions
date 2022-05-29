#My solution
def revers_s(s):
    new = s.split(" ")
    newst = []
    ser = []
    for i in range(len(new)-1):
        newst.append(list(new[i]))
    for j in range(len(newst)-1):
        newst[j].reverse()
    for w in range(len(newst)):
        ser.append("".join(newst[w]))
    return " ".join(ser)
s = "Let's take LeetCode contest"
print(revers_s(s))

#Other solution
def reverseWords(self, s: str) -> str:
    mylist = s.split()
    reverse_list = [each[::-1] for each in mylist]
    return " ".join(reverse_list)