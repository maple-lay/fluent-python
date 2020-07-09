"""
    建立由列表组成的列表

"""

if __name__ == '__main__':

    my_list = [["_"] * 3 for i in range(3)]
    print(my_list)
    my_list[1][2] = "X"
    print(my_list)

    # 等价于：
    board = []
    for i in range(3):
        row = ["_"] * 3
        board.append(row) # 每次迭代都创建一个新的列表迭代

    # Demo 2- 13
    # 错误的方式
    # 列表内的三个列表指向同一个引用
    my_list2 = [["_"] *3] * 3
    print(my_list2)
    my_list2[1][2] = "X"
    print(my_list2)

    # 等价于：
    row2 = ['_'] * 3
    board2 = []
    for i in range(3):
        board2.append(row2) # 每次迭代加入的都是形同的列表