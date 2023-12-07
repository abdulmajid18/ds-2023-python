import collections


def total_fruits(fruits):
    count = collections.defaultdict(int)
    l, total_count, res = 0, 0, 0

    for r in range(len(fruits)):
        count[fruits[r]] += 1
        total_count += 1

        while len(count) > 2:
            f = fruits[l]
            count[f] -= 1
            total_count -= 1
            l += 1
            if not count[f]:
                count.pop(f)

        res = max(res, total_count)
    return res