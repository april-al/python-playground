def bubble_sort(ar):
    for i in range(len(ar)):
        for j in range(len(ar) - 1):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]

    return ar


def bubble_sort_tmp(ar):
    for i in range(len(ar)):
        for j in range(len(ar) - 1):
            tmp = ar[j]
            if ar[j] > ar[j + 1]:
                ar[j] = ar[j + 1]
                ar[j + 1] = tmp

    return ar


tst = [2, 8, 6, 7, 4, -1, 90, -50, 900, 55]
res = bubble_sort(tst)
print(res)

tst2 = [2, 8, 6, 7, 4, -1, 90, -50]
res2 = bubble_sort_tmp(tst2)
print(res2)
