"""
给一个日期，判断是今年的第几天

"""


def tolDay():
    input_date = input("请输入日期：")

    date = input_date.split(".")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    tolday = 0
    isLeap = True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False
    for i in range(1, month):
        if i in [1, 3, 5, 7, 8, 10, 11]:
            tolday += 31
        elif isLeap and i == 2:
            tolday += 29
        elif not isLeap and i == 2:
            tolday += 28
        else:
            tolday += 30
    return tolday + day


print(tolDay())
