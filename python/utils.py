#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

from collections import deque


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        res, node = [], self
        while node:
            res.append(str(node.val))
            node = node.next
        return 'List[%s]' % ', '.join(res)


class List(object):

    def __init__(self, vals):
        head = node = ListNode(0)
        for val in vals:
            node.next = ListNode(val)
            node = node.next
        self.head = head.next


class TreeNode(object):

    def __init__(self, x, formatter=int):
        self.val = formatter(x)
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode(%s)[%s, %s]' % (
            self.val,
            self.left,
            self.right,
        )


class Tree(object):

    def __init__(self, s):

        if not s:
            return

        self.root = TreeNode(s[0])
        i, l, st = 1, len(s), deque([self.root])

        def _parseNode(val):
            if val == '#':
                return None
            node = TreeNode(val)
            st.append(node)
            return node

        while st and i < l:
            node = st.popleft()
            node.left = _parseNode(s[i])
            if i + 1 < l:
                node.right = _parseNode(s[i + 1])
            i += 2