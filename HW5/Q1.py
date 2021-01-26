############
# QUESTION 1
############

def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(
        ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "|" + rs * "_" + (
                rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"


class Binary_search_tree():

    def __init__(self):
        self.root = None

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out

    def lookup(self, key):
        """ return node with key, uses recursion """

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        """ insert node with key,val into tree, uses recursion """

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val  # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else:  # key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return

        if self.root == None:  # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)

    def diam(self):
        diameter = 0

        def diam_rec(node):
            nonlocal diameter
            if node is None:
                return 0
            opt1 = diam_rec(node.left)
            opt2 = diam_rec(node.right)
            diameter = diameter if diameter > (opt1 + opt2 + 1) else \
                (opt1 + opt2 + 1)
            depth = 1 + opt1 if opt1 > opt2 else 1 + opt2
            return depth

        diam_rec(self.root)
        return diameter

    def is_min_heap(self):

        def is_min_heap_rec(node):
            if node is None:
                return True
            if (node.left is not None and node.val > node.left.val) or \
                    (node.right is not None and node.val > node.right.val):
                val = False
            else:
                val = True
            return val and is_min_heap_rec(node.left) and \
                   is_min_heap_rec(node.right)

        return is_min_heap_rec(self.root)

# cur_max = 0
#
# def diam_rec(node):
#     nonlocal cur_max
#     if node is None:
#         return 0
#     left = diam_rec(node.left)
#     right = diam_rec(node.right)
#     cur_max = max(cur_max, 1 + left + right)
#     return 1 + max(left, right)
#
# return max(diam_rec(self.root), cur_max)

# t1 = Binary_search_tree()
# t1.insert('d', 1)
# t1.insert('b', 2)
# t1.insert('a', 17)
# t1.insert('c', 19)
# t1.insert('f', 3)
# t1.insert('e', 36)
# t1.insert('g', 7)
# print(t1)
# print(t1.diam())
#
# t2 = Binary_search_tree()
# t2.insert('c', 10)
# t2.insert('a', 10)
# t2.insert('b', 10)
# t2.insert('g', 10)
# t2.insert('e', 10)
# t2.insert('d', 10)
# t2.insert('f', 10)
# t2.insert('h', 10)
# print(t2)
# print(t2.diam())
# #
# t3 = Binary_search_tree()
# t3.insert('c', 1)
# t3.insert('g', 3)
# t3.insert('e', 5)
# t3.insert('d', 7)
# t3.insert('f', 8)
# t3.insert('h', 6)
# t3.insert('z', 6)
# print(t3)
# print(t3.diam())
# t4 = Binary_search_tree()
# t4.insert('a', 1)
# t4.insert('b', 3)
# t4.insert('c', 5)
# t4.insert('d', 7)
# t4.insert('e', 8)
# t4.insert('f', 6)
# t4.insert('g', 6)
# print(t4)
# print(t4.diam())
