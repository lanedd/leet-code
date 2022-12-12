from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        total_water = 0
        l_i = 0
        height_len_m_1 = len(height) - 1
        r_i = height_len_m_1
        l_max = height[l_i]
        r_max = height[r_i]
        index = 0
        # Determine water height at each location
        while index < height_len_m_1:
            if height[l_i] < height[r_i]:
                total_water += l_max - height[l_i]
                l_i += 1
                l_max = max(l_max, height[l_i])
            else:
                total_water += r_max - height[r_i]
                r_i -= 1
                r_max = max(r_max, height[r_i])
            index += 1

        return total_water


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if len(height) == 0:
#             return 0
#         water_height = [None] * len(height)
#         l_i = 0
#         r_i = len(height) - 1
#         l_max = height[l_i]
#         r_max = height[r_i]
#         index = 0
#         # Determine water height at each location
#         while index < len(height):
#             if height[l_i] < height[r_i]:
#                 water_height[l_i] = l_max
#                 l_i += 1
#                 l_max = max(l_max, height[l_i])
#             else:
#                 water_height[r_i] = r_max
#                 r_i -= 1
#                 r_max = max(r_max, height[r_i])
#             index += 1
#
#         total_water = 0
#         for index in range(len(height)):
#             total_water += max(0, water_height[index] - height[index])
#
#         return total_water

for my_input, ans in [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([], 0)
]:
    my_sol = Solution().trap(my_input)
    print(my_sol, ans)
