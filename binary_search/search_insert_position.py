def sertInsearchPosition(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        gues = nums[mid]

        if target == gues:
            return mid
        if target < gues:
            end = mid - 1
        else:
            start = mid + 1
    return start


a = [x for x in range(1,10,2)]
print(sertInsearchPosition(a, 2))



