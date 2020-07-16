"""
https://leetcode.com/problems/powx-n/
快速幂运算:
Example 5**3=?
指数部分3的二进制是11
所以result=5**1+5**2
"""
import random
import unittest


# 假设幂的基数x>0
def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    is_negative = n < 0
    if is_negative:
        n = -n

    result = 1
    base = x
    while n != 0:
        # 幂运算结果等于指数的二进制为1的位 的加权乘积
        # 例如 5**3 = 5**1 * 5**2
        if n % 2 == 1:
            result *= base
        base *= base
        n //= 2
    if is_negative:
        return 1 / result
    else:
        return result


class Testing(unittest.TestCase):
    def test_my_pow(self):
        base = random.uniform(1, 10)
        power = random.randint(-10, 10)
        # print(base, power)
        # self.assertEqual(base ** power, my_pow(base, power))
        self.assertLessEqual(abs(base ** power - my_pow(base, power)), 1e-3)