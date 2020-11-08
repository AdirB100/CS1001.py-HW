import time


# 1st solution
def f1(num):
    cnt_t=0
    for i in range(1000):
        t0 = time.perf_counter()
        m = num
        cnt = 0
        while m > 0:
            if m % 10 == 0:
                cnt = cnt + 1
            m = m // 10
        t1 = time.perf_counter()
        cnt_t+=t1-t0
    print(num, 'has', cnt, "zeros")
    print("Running time: ", cnt_t/1000, 'sec')


# 2nd solution
def f2(num):
    cnt_t=0
    for i in range(1000):
        t0 = time.perf_counter()
        cnt = 0
        snum = str(num)  # num as a string
        for digit in snum:
            if digit == "0":
                cnt = cnt + 1
        t1 = time.perf_counter()
        cnt_t+=t1-t0
    print(num, 'has', cnt, "zeros")
    print("Running time: ", cnt_t/1000, 'sec')


# 3rd solution
def f3(num):
    cnt_t=0
    for i in range(1000):
        t0 = time.perf_counter()
        cnt = str.count(str(num), "0")
        t1 = time.perf_counter()
        cnt_t+=t1-t0
    print(num, 'has', cnt, "zeros")
    print("Running time: ", cnt_t/1000, 'sec')


# for i in [2 ** 200, 2 ** 400, 2 ** 800, 2 ** 1600]:
#     f3(i)

# for i in [72567176, 14560756, 75264070, 70904560, 80600504, 40800001, 10000002, 50000000]:
#     f1(i)
