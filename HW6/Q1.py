############
# QUESTION 1
############

# (a)
def take_only(gen, predicate, n):
    cnt = 0
    for element in gen:
        if cnt == n:
            break
        if predicate(element):
            yield element
            cnt = 0
        else:
            cnt += 1


# def take_only(gen, predicate, n):
#     cnt = 0
#     vals = []
#     for i in gen:
#         if cnt >= n:
#             break
#         if predicate(i):
#             vals.append(i)
#             cnt = 0
#         else:
#             cnt += 1
#     for i in vals:
#         yield i


# next_object = next(gen)
# if predicate(next_object):
#     yield next_object
#     cnt = 0
# else:
#     cnt += 1


assert list(take_only((i for i in range(30)), lambda x: x % 3 == 1, 5)) == \
       [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
assert list(
    take_only((i for i in range(30)), lambda x: x < 10 or x % 7 == 0, 5)) == \
       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14]
my_gen = take_only((i for i in range(30)), lambda x: x > 10 or x == 0, 5)
test_lst = [g for g in my_gen]
assert test_lst == [0]


# (b)
def blocks(gen, k):
    block = []
    flag = 0
    for element in gen:
        flag = 0
        block.append(element)
        if len(block) == k:
            yield block
            block = []
            flag = 1
    if flag == 0:
        yield block


assert list(blocks((i for i in range(10)), 5)) == [[0, 1, 2, 3, 4],
                                                   [5, 6, 7, 8, 9]]
assert list(blocks((i for i in range(10)), 3)) == [[0, 1, 2], [3, 4, 5],
                                                   [6, 7, 8], [9]]
assert list(blocks((i for i in range(9)), 3)) == [[0, 1, 2], [3, 4, 5],
                                                  [6, 7, 8]]

# Test
import types

# (a)
if not isinstance(take_only((i for i in range(30)), lambda x: x % 3 == 1, 5),
                  types.GeneratorType):
    print("Error in take_only")
if list(take_only((i for i in range(30)), lambda x: x % 3 == 1, 5)) != \
        [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]:
    print("Error in take_only")
if list(take_only((i for i in range(30)), lambda x: x < 10 or x % 7 == 0, 5)) \
        != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14]:
    print("Error in take_only")
# (b)
if not isinstance(blocks((i for i in range(10)), 5), types.GeneratorType):
    print("Error in blocks")
if list(blocks((i for i in range(10)), 5)) != [[0, 1, 2, 3, 4],
                                               [5, 6, 7, 8, 9]]:
    print("Error in blocks")
if list(blocks((i for i in range(10)), 3)) != \
        [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
    print("Error in blocks")
if list(blocks((i for i in range(9)), 3)) != [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
    print("Error in blocks")
