############
# QUESTION 2
############

# Part A
class PNode:

    def __init__(self, val, p, next=None):
        self.value = val
        self.next = next
        self.priority = p

    def __repr__(self):
        return f"{self.value},{self.priority} ({id(self)})"
    # This shows pointers as well for educational purposes


class PQueue:

    def __init__(self, vals=None, ps=None):
        self.next = None
        self.len = 0
        if vals is not None:
            for val, p in zip(vals, ps):
                self.insert(val, p)

    def __len__(self):
        return self.len

    def __repr__(self):
        out = ""
        p = self.next
        while p != None:
            out += str(p) + ", "  # str(p) envokes __repr__ of class PNode
            p = p.next
        return "[" + out[:-2] + "]"

    def pull(self):
        if self.next is None:
            return None, None
        tmp = self.next
        self.next = self.next.next
        tmp.next = None
        self.len -= 1
        return tmp.value, tmp.priority

    def insert(self, val, p):
        tmp = self.next
        node = PNode(val, p)
        if (tmp is None) or (node.priority > tmp.priority):
            node.next = self.next
            self.next = node
            self.len += 1
            return
        while tmp.next is not None:
            if node.priority > tmp.next.priority:
                node.next = tmp.next
                tmp.next = node
                break
            tmp = tmp.next
        if tmp.next is not node:
            node.next = tmp.next
            tmp.next = node
        self.len += 1


# import time
#
# ls1=PQueue()
# ls2=PQueue()
# for i in range(4000):
#     ls1.insert('A',5)
# for i in range(8000):
#     ls2.insert('B',5)
#
# t0=time.perf_counter()
# ls1.insert('X',4)
# t1=time.perf_counter()
# print(t1-t0)
#
# t0=time.perf_counter()
# ls2.insert('Y',4)
# t1=time.perf_counter()
# print(t1-t0)

# def pull(self):
#     tmp = cnt = cnt2
#     p = self.next
#     while p is not N
#         if p.priorit
#             tmp = p.
#             cnt2 = c
#         p = p.next
#         cnt += 1
#     p = self.next
#     if cnt2 == 0:
#         tmp = self.n
#         self.next =
#     else:
#         for i in ran
#             p = p.ne
#         tmp = p.next
#         p.next = p.n
#     return tmp.value
# def insert(self, val
#     tmp = self.next
#     node = PNode(val
#     self.next = node
#     self.len += 1

# pq = PQueue("abc", [2, 3, 3])

#  Part B
class Node():
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        # return str(self.value)
        # This shows pointers as well for educational purposes:
        return "(" + str(self.value) + ", next: " + str(id(self.next)) + ")"


class Linked_list():
    def __init__(self, seq=None):
        self.next = None
        self.len = 0
        if seq is not None:
            for x in seq[::-1]:
                self.add_at_start(x)

    def __repr__(self):
        out = ""
        p = self.next
        while p is not None:
            out += str(p) + ", "  # str(p) invokes __repr__ of class Node
            p = p.next
        return "[" + out[:-2] + "]"

    def __len__(self):
        """ called when using Python's len() """
        return self.len

    def add_at_start(self, val):
        """ add node with value val at the list head """
        p = self
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.len += 1

    def reverse_start_end(self, k):
        n = self.len
        assert 0 <= k <= n / 2
        if k <= 1:
            return
        # k >= 2; n >= 4
        # first part
        tmp1 = self.next
        tmp2 = tmp3 = tmp1.next
        for i in range(k - 1):
            tmp3 = tmp3.next
            tmp2.next = tmp1
            tmp1 = tmp2
            tmp2 = tmp3
        tmp2 = self.next
        self.next = tmp1
        tmp2.next = tmp3
        # second part
        for i in range(n - 2 * k):
            tmp2 = tmp2.next
        tmp0 = tmp2
        tmp1 = tmp0.next
        tmp2 = tmp3 = tmp1.next
        for i in range(k - 1):
            tmp3 = tmp3.next
            tmp2.next = tmp1
            tmp1 = tmp2
            tmp2 = tmp3
        tmp2 = tmp0.next
        tmp0.next = tmp1
        tmp2.next = tmp3

# import time
# ls=Linked_list('a'*1000)
# ls2=Linked_list('a'*2000)
# t0=time.perf_counter()
# ls.reverse_start_end(500)
# t1=time.perf_counter()
# print(t1-t0)
# t0=time.perf_counter()
# ls2.reverse_start_end(1000)
# t1=time.perf_counter()
# print(t1-t0)


# def reverse_start_end(self, k):
#     assert 0 <= k <= self.len / 2
#     if k <= 1:
#         return
#     # first part
#     tmp1 = self.next
#     tmp2 = self.next
#     for i in range(k - 1):
#         tmp2 = tmp2.next
#     self.next = tmp2
#     tmp2 = tmp1.next
#     tmp1.next = self.next.next
#     tmp3 = tmp2.next
#     while tmp3 is not self.next.next:
#         tmp2.next = tmp1
#         tmp1 = tmp2
#         tmp2 = tmp3
#         tmp3 = tmp2.next
#     self.next.next = tmp1
#     # second part
#     for i in range(len(self)-1):
#         tmp2 = tmp2.next
#         if i == len(self)-k-2:
#             tmp4 = tmp2
#         if i == len(self)-k-1:
#             tmp1 = tmp2
#     #
#     tmp3 = tmp1.next
#     tmp1.next = None
#     tmp5 = tmp3.next
#     while tmp5 is not tmp2:
#         tmp3.next = tmp1
#         tmp1 = tmp3
#         tmp3 = tmp5
#         tmp5 = tmp3.next
#     tmp3.next = tmp1
#     tmp5.next = tmp3
#     tmp4.next = tmp5

# ls = Linked_list('abcdefghijklm')

# #  Part C
# class Node2:
#     def __init__(self, val):
#         self.value = val
#         self.next1 = None
#         self.next2 = None
#
#     def __repr__(self):
#         # return str(self.value)
#         # This shows pointers as well for educational purposes:
#         return "(" + str(self.value) + ", next1: " + str(id(self.next1)) + \
#                ", next2: " + str(id(self.next2)) + ")"
#
#
# class Forked_list:
#     def __init__(self)
#         self.next = None
#         self.len = 0
#
#     def __len__(self):
#         """ called when using Python's len() """
#         return self.len
#
#     def cycle(self, val):
#         tmp1 = tmp2 = self.next
#         while tmp1.next1 is None or tmp1.next2 is None:
#             if tmp1.next1 is not None:
#                 tmp1 = tmp2 = tmp1.next1
#             elif tmp1.next2 is not None:
#                 tmp1 = tmp2 = tmp1.next2
#             else:
#
