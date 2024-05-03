def find_kth_latgest_1(nums, k):
    nums.sort()
    return nums[len(nums)-k]


def find_kth_largest_two(nums, k):
    k = len(nums) - k

    def quick_select(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            quick_select(l, p-1)
        elif p < k:
            quick_select(p+1, r)
        else:
            return nums[p]

    return quick_select(0, len(nums) - 1)


import heapq


def kth_largest(nums, k):
    # Build a min-heap containing the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # Process remaining elements in the array
    for num in nums[k:]:
        if num > min_heap[0]:
            # Replace the root with the current element
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    # Return the kth largest element
    return min_heap[0]


# Example usage:
def chunk_string(string, chunk_size):
    """Breaks a string into chunks of specified size without splitting words."""
    chunks = []
    while len(string) > chunk_size:
        # Find the index of the last occurrence of "--" before the chunk_size
        last_hyphen_index = string.rfind('--', 0, chunk_size)
        if last_hyphen_index == -1:
            # If no "--" found, split at chunk_size
            last_hyphen_index = chunk_size
        chunks.append(string[:last_hyphen_index])
        # Remove the processed chunk from the string
        string = string[last_hyphen_index + 2:]  # Move beyond the "--"
    chunks.append(string)
    return chunks


def send_chunks(chunks):
    """Simulates sending each chunk."""
    for chunk in chunks:
        print("Sending chunk:", chunk)
        # Replace the print statement with your actual sending mechanism

new = ['brk_fee_intraday', 'ca_ircrv_intraday', 'crd_tr_intraday', 'cs_fut_intraday', 'cs_sub_intraday', 'eqd_exo_intraday', 'eqd_tr_intraday', 'gn_indx_intraday',
       'ird_exo_intraday', 'ird_tr_intraday', 'mop_add_fl_intraday', 'mv_intraday_',
       'mx_eqidx_intraday', 'mx_extcat_intraday', 'mx_fx_intraday', 'mx_iridx_intraday', 'mx_strats_intraday', 'pl_intraday_', 'pl_intraday_calc', 'tr_intraday', 'xg_intraday']
# input_string = "--".join(new)
# print(input_string)
# chunk_size = 80
#
# # Break the string into chunks
# chunks = chunk_string(input_string, chunk_size)
#
# # Send each chunk
# send_chunks(chunks)

import json

tables = {"a": "one", "b": "two"}

result = json.dumps(tables)
result2 = str(tables)
print(type(result))
print(type(result2))
print(result == result2)


