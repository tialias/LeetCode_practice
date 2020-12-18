# 暴力快排
import random


def quicjSort(array):
    if not array:
        return []
    else:
        pivot = array[0]
        lowsort = [i for i in array[1:] if i < pivot]

        highsort = [i for i in array[1:] if i >= pivot]

    return quicjSort(lowsort) + [pivot] + quicjSort(highsort)


a = list(range(20))
random.shuffle(a)

print(a)
print(quicjSort(a))
