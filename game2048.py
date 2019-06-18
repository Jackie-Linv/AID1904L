"""
2048游戏核心算法
"""


# 1.定义函数，将列表中0元素移至末尾
def zero_to_end(list_target):
    # 删除0元素，再末尾添0
    for i in range(len(list_target) - 1, -1, - 1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)


# list01 = [2, 2, 0, 2]
# zero_to_end(list01)
# print(list01)


# 定义函数，合并列表中相同元素
def combine_number(list_target):
    zero_to_end(list_target)
    for i in range(len(list_target) - 1):
        if list_target[i] == list_target[i + 1]:
            list_target[0] += list_target[1]
            del list_target[i + 1]
            list_target.append(0)


# list01 = [2, 2, 0, 2]
# combine_number(list01)
# print(list01)

def move_left(map):
    for row in map:
        combine_number(row)


