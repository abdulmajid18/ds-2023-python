def summaryRange(nums):
    res = []

    for num in nums:
        if not res or num != res[-1][-1] + 1:
            if res and len(res[-1]) >= 2:
                res[-1] = [res[-1][0]] + [res[-1][-1]]
            res.append([num])
        else:
            res[-1].append(num)

    if res and len(res[-1]) >= 2:
        res[-1] = [res[-1][0]] + [res[-1][-1]]
    print(['->'.join(map(str,x)) for x in res])
    return ['->'.join(map(str,x)) for x in res]

if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    summaryRange(nums)
