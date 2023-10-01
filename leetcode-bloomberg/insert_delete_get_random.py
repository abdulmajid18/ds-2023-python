import random


class RandomizedSet:

    def __int__(self):
        self.num_map = {}
        self.num_list = []

    def insert(self, val):
        res = val not in self.num_map
        if res:
            self.num_map[val] = len(self.num_list)
            self.num_list.append(val)
        return res

    def remove(self, val):
        res = val in self.num_map
        if res:
            idx = self.num_map[val]
            last_val = self.num_list[-1]
            self.num_list[idx] = last_val
            self.num_map.pop()
            self.num_list[last_val] = idx
            del self.num_list[val]
        return res

    def get_random(self):
        return random.choice(self.num_list)
