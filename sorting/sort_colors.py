import unittest
from copy import deepcopy
from typing import List

# 思路，把所有2挪到右边，把所有0挪到左边，那么剩余的1就刚好在中间了
# 需要三根指针，左右以及curr
# 若nums[curr] = 0 则将其与 nums[p0]互换；
# 若nums[curr] = 2 则与 nums[p2]互换。
def partition(nums: List[int]):
    size = len(nums)
    left, right, current = 0, size-1, 0

    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
        elif nums[current] == 2:
            nums[right], nums[current] = nums[current], nums[right]
            right -= 1
        current += 1



class UnitTest(unittest.TestCase):
    TEST_CASES = [
        [1, 2, 0],
        [1, 0, 1, 2],
        [2, 0, 2, 1, 1, 0]
    ]

    def test(self):
        for nums in deepcopy(self.TEST_CASES):
            input_nums = deepcopy(nums)
            partition(input_nums)
            self.assertEqual(sorted(nums), input_nums)
