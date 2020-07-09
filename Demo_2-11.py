"""
    对seq[start:stop:step]求值，Python调用seq.__getitem(slice(start, stop, step))
    如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象。即便只有单独一个值，也要把它转换成可迭代的序列
"""

if __name__ == '__main__':
    abc = '''
    0.....6.................................40...........52...55........
    1909   Pimoroni Pibrella                  $17.50       3     $52.5
    1489   6mm Tactile Switch x20               $4.95       2     $9.9
    '''
    # 点个数没数对...

    SKU = slice(0, 6)
    DESCRIPTION = slice(10, 40)
    UNIT_PRICE = slice(40, 52)
    QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)

    line_items = abc.split("\n")[2:]
    for item in line_items:
        print(item[UNIT_PRICE], item[DESCRIPTION])