#My solution
def mine(nums):
    return sorted([x ** 2 for x in nums])

# Two Pointers method

def other(nums):
    # return sorted(x*x for x in nums)
    n = len(nums)
    sorted = [0] * n
    left = 0
    right = n - 1
    for i in range(0,n):
        if abs(nums[left]) < abs(nums[right]):
            print(abs(nums[left]), "<", abs(nums[right]))
            squared = nums[right] * nums[right]
            right -= 1
        else:
            print(abs(nums[left]),">=", abs(nums[right]))
            squared = nums[left] * nums[left]
            left += 1
        sorted[i] = squared
    return sorted
arr = [-4,-1,0,3,10]
print(mine(arr))
print(other(arr))

# def other(nums):
#     # return sorted(x*x for x in nums)
#     n = len(nums)
#     sorted = [0] * n
#     left = 0
#     right = n - 1
#     for i in range(n - 1, -1, -1):
#         if abs(nums[left]) < abs(nums[right]):
#             print(abs(nums[left]), "<", abs(nums[right]))
#             squared = nums[right] * nums[right]
#             right -= 1
#         else:
#             print(abs(nums[left]),">=", abs(nums[right]))
#             squared = nums[left] * nums[left]
#             left += 1
#         sorted[i] = squared
#     return sorted
# arr = [-4,-1,0,3,10]
# print(mine(arr))
# print(other(arr))