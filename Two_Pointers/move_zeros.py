def move(nums):
    zeros_count = nums.count(0)
    next_non_zero = 0
    for n in nums:
        if n != 0:
            nums[next_non_zero] = n
            next_non_zero += 1
    for zero in range(1, zeros_count + 1):
        nums[-zero] = 0

nums = [0,1,0,3,12]
print(move(nums))

a = [15] * 9
print(sum(a))