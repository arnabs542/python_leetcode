"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
给n个整数的山脉数组，即先增后减的序列，找到山顶(最大值)
"""

import unittest
from typing import List


def peak_index_brute_force(nums: List[int]) -> int:
    i = 0
    while nums[i] < nums[i + 1]:
        i += 1
    return i


def peak_index(nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        middle = start + (end - start) // 2
        print(start, middle, end)
        if nums[middle] > nums[start]:
            # 山峰在[middle,end]之间，包含middle
            start = middle
        else:
            # 山峰在[start,middle)
            end = middle - 1
    return start


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([24, 69, 100, 99, 79, 78, 67, 36, 26, 19], 2),
        ([0, 1, 0], 1),
        ([0, 2, 1, 0], 1),
    ]

    def test_peak_index_brute(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, peak_index_brute_force(nums))

    def test_peak_index(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, peak_index(nums))