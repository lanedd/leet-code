# from bisect import bisect_left
import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_i = 0
        nums2_i = 0
        index = 0
        total_len = len(nums1) + len(nums2)
        half_len = math.ceil(total_len / 2)
        this_num = None

        if (total_len % 2) == 0:
            average = True
        else:
            average = False

        while index < half_len:
            if nums2_i >= len(nums2):
                # Find answer in nums1
                ans_i = nums1_i + (half_len - 1 - index)
                if average:
                    return (nums1[ans_i] + nums1[ans_i + 1]) / 2
                else:
                    return nums1[ans_i]
            if nums1_i >= len(nums1):
                # Find answer in nums2
                ans_i = nums2_i + (half_len - 1 - index)
                if average:
                    return (nums2[ans_i] + nums2[ans_i + 1]) / 2
                else:
                    return nums2[ans_i]

            if nums1[nums1_i] > nums2[nums2_i]:
                this_num = nums2[nums2_i]
                nums2_i += 1
            else:
                this_num = nums1[nums1_i]
                nums1_i += 1
            index += 1

        if average:
            if nums1_i < len(nums1) and nums2_i < len(nums2):
                next_num = min(nums1[nums1_i], nums2[nums2_i])
            elif nums1_i < len(nums1):
                next_num = nums1[nums1_i]
            else:
                next_num = nums2[nums2_i]
            return (this_num + next_num) / 2
        else:
            return this_num

for array1, array2, answer in [
    [[1,3], [2], 2],
    [[1,2], [3,4], 2.5],
    [[0,0], [0,0], 0],
    [[], [1], 1],
    [[2], [], 2],
    [[1,2,3,4], [1], 2],
    [[100001], [100000], (100001 + 100000) / 2],
    [[2,3], [1], 2],
    [[100001], [100000], (100001 + 100000) / 2],
    [[1], [2, 3], 2],
    [[], [1,5,6,7], 5.5],
    [[2,6,7,8], [], 6.5],
    [[], [1,2,3], 2],
    [[1,2,3], [], 2],
]:
# array1 = [1, 3, ]
# array1 = [1, 3, 5, 6, 7]
# array2 = [2, ]
    sol = Solution().findMedianSortedArrays(array1, array2)
    print(sol, answer)
