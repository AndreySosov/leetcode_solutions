def isBadVersion(version):
    gues = [3,4,5,6,7,8]

    if version in gues:
        return True
    return False



def firstBadVersion(n: int) -> int:
    start = 1
    end = n

    while start <= end:
        mid = (start + end) // 2

        if isBadVersion(mid):
            end = mid - 1
        else:
            start = mid + 1
    return start

print(firstBadVersion(15))