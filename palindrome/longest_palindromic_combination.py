"""
https://www.lintcode.com/problem/longest-palindrome
输入一个字符串，通过组合字符串的每个字符，求出这些组合中最长回文串的长度
例如: cbbd的组合中，最长是3(bcb或bdb)

## 贪心算法
回文串中，每个字符要么出现奇数次，要么出现偶数次
可以借鉴桶排序/计数排序，定义一个ASCII的table记录每个字符的出现次数
最长回文串的组合可能是：奇数出现次数的最大值+所有偶数出现次数之和
FIXME 更正下奇数次出现次数的情况：
奇数次出现时，例如出现了3次，实际上可以3-1=2变成偶数次并记入最长回文组合中
所以奇数次出现时，有一个奇数是全取，剩余奇数次都是-1后变成偶数并记入最长回文组合中
写法1：设一个is_odd_occur的布尔值，if-else语句的奇数分支中将is_odd_occur设为true，返回值时根据is_odo_occur决定结果是否+1
写法2：如果result是偶数而且出现次数是奇数，那么ans+1
这就是贪心算法，自己先假定一种数学公式/规律能获得最大值，贪心算法最怕自己的想法是错的，就像我最初版本的贪心奇数次情况完全错的

## collections.Counter
统计每个元素出现次数的可以用python的Counter数据结构
"""
import unittest
import collections


def solution(s: str) -> int:
    size = len(s)
    if size <= 1:
        return size
    ascii_table = [0 for _ in range(ord('z')+1)]
    for i in range(size):
        ascii_table[ord(s[i])] += 1
    # 奇数次出现次数的最大值
    max_odd = 0
    result = 0
    for i in range(ord('A'), ord('z')+1):
        if ascii_table[i] == 0:
            continue
        if ascii_table[i] % 2 == 0:
            result += ascii_table[i]
        else:
            if ascii_table[i] > max_odd:
                max_odd = ascii_table[i]
    result += max_odd
    return result


def other_solution(s):
    # cnt统计字符串s中每种字母出现次数的计数数组
    # OddCount为是否有奇数次字符，1表示有，0表示无
    # ans为最终答案
    ans = 0
    counter = collections.Counter(s)
    print(counter)
    print(counter.values())
    # 每种字符可使用cnt/2*2次
    # 如果遇到出现奇数次的字符并且中心位置空着，那么答案加1
    for i in counter.values():
        # 这里比较妙，直接整合了奇数和偶数次情况
        ans += i // 2 * 2
        if ans % 2 == 0 and i % 2 == 1:
            ans += 1
    return ans


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("abccccdd", 7),  # dccaccd
        ("cbbd", 3),  # bcb/bdb
        #("NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy", 39)
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], other_solution(case[0]))
