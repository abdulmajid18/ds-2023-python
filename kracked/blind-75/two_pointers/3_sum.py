class SolutionBruteForce:
    def threeSum(self, nums):
        n = len(nums)
        result = set()  # Using a set to store unique triplets

        # Iterate through all triplets (i, j, k)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))  # Sort to avoid duplicates
                        result.add(triplet)  # Store only unique triplets

        return list(result)  # Convert set to list for output

