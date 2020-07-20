import unittest
import sys
from typing import List


def solution(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    size = len(nums)
    min_diff = sys.maxsize
    closest_sum = 0
    for i in range(size - 2):
        left, right = i + 1, size - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            new_diff = abs(three_sum - target)
            if new_diff < min_diff:
                min_diff = new_diff
                closest_sum = nums[i] + nums[left] + nums[right]
            if three_sum > target:
                right -= 1
            elif three_sum < target:
                left += 1
            else:
                return closest_sum
    return closest_sum


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([-1, 2, 1, -4], 2, 2),
        ([2, 7, 11, 15], 3, 20),
    ]

    def test(self):
        for nums, target, expected in self.TEST_CASES:
            self.assertEqual(expected, solution(nums, target))
