"""
匿名函数
    lambda
    Python简单的句法限制了lambda函数的定义体只能使用纯表达式
    lambda函数的定义体中不能赋值，也不能使用while和try等Python语句

    lambda表达式重构秘笈如果使用lambda表达式导致一段代码难以理解，Fredrik Lundh建议像下面这样重构。
        (1)编写注释，说明lambda表达式的作用。
        (2)研究一会儿注释，并找出一个名称来概括注释。
        (3)把lambda表达式转换成def语句，使用那个名称来定义函数。
        (4)删除注释。
"""

if __name__ == '__main__':
    fruits = ['strawberry', 'fig', 'apple', 'raspberry', 'banana']
    print(sorted(fruits, key=lambda word: word[::-1]))