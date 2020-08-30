"""
https://leetcode-cn.com/problems/plus-one/
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。


"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        su = 1
        for i in range(len(digits)-1,-1,-1):
            tmp = digits[i]
            tmp += su
            if tmp >= 10:
                su = 1
                digits[i] = tmp-10
                if i == 0:
                    digits = [1] + digits
            else:
                su = 0
                digits[i] = tmp
                break
        return digits