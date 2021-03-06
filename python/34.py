#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = self.binarySearch(nums, target, lambda x, y: x < y)
        r = self.binarySearch(nums, target, lambda x, y: x <= y) - 1
        if l > r:
            return [-1, -1]
        return [l, r]

    def binarySearch(self, nums, target, func):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) / 2
            if func(nums[mid], target):
                l = mid + 1
            else:
                r = mid
        return l


a = [1, 2, 2, 4, 5, 5, 6, 7, 8]
print Solution().searchRange(a, 3)
