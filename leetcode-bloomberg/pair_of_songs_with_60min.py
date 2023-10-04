from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        map_track = defaultdict(int)
        for i in range(len(time)):
            time[i] %= 60
            map_track[time[i]] += 1
        count = 0
        for k, v in map_track.items():
            if k == 0 or k == 30:
                count += ((v-1) * (v) ) // 2
            elif k < 30 and (60-k) in map_track:
                new_count = v * map_track[60-k]
                count +=  new_count
        return count
