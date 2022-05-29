#My solution
def two_sum(nums, target):
    start = 0
    end = start + 1
    while start < end:
        st = nums[start]
        en = nums[end]
        if nums[start] + nums[end] == target:
            return [start+1, end+1]
        elif nums[start] + nums[end] < target:
            if end >= len(nums)-1:
                start += 1
                end = start+1
            else:
                end += 1
        elif nums[start] + nums[end] > target:
            if nums[end] > target:
                start += 1
                end = start+1
            else:
                end += 1

def other_solution(nums, target):
    start = 0
    end = len(numbers)-1
    sum = 0
    while start != end :
        sum = numbers[start] + numbers[end]
        if sum > target:
            end -= 1
        elif sum < target:
            start +=1
        else:
            return [start+1,end+1]

nums = [0,3,4,5,9,15]
nums1 = [5,25,75]
nums2 = [0,0]
target = 100

print(two_sum(nums1,target))
