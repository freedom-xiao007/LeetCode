#!/usr/bin/env python
# @Time    : 2019/3/27 8:45
# @Author  : LiuWei
# @Site    : 
# @File    : reverseStr.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# 541. 反转字符串 II
"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the
start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and left the other as original.

给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。
如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:
    该字符串只包含小写的英文字母。
    给定字符串的长度和 k 在[1, 10000]范围内。

k = 1 : 2 K 2K
adbdefg -> bacdefg
k = 2 : 4 K 2K
bacdefg -> abcdefg
k = 3 : 6 K 2K
abcdefg > cbadefg
k = 4 : 8
cbad efg > dabcefg
K = 5 : 10
dabce fg > ecbad fg
K = 6 : 12
ecbadf g > fdabceg
K = 7 : 14
gecbadf
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str: