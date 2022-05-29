#My solution
a = [1,2,3,4,5,6,7]
nums = [-1,-100,3,99]
def rotate(arr, k):
    b = [0]*k
    new = b+arr
    index = k-1
    for i in range(len(new)-1,len(new)-k-1,-1):
        new[index]=new.pop(i)
        index -= 1
    return new
print(rotate(a,1))

#Other guy solution
# def rotate(nums, k):
#     k = k % len(nums)
#     i = 0
#     while i < k:
#         temp = nums.pop()
#         nums.insert(0, temp)
#         i += 1

def rotate(nums, k):
    k = k%len(nums)
    i = 0
    while i < k:
        temp = nums.pop()
        nums.insert(0, temp)
        i += 1