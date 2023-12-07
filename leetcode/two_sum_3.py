from collections import defaultdict


class TwoSumInternalDataStructure:
    def __int__(self):
        self.hash_table = {}

    def add_element(self, num):
        for elem in num:
            self.hash_table.get(elem, 0) + 1

    def find_elements(self, target):
        for key, value in self.hash_table.items():
            number = target - key
            if number == key:
                if self.hash_table.get(number) >= 2:
                    return True
            elif self.hash_table[number]:
                return True
        return False
