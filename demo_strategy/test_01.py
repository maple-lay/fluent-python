"""
测试 strategy_01
"""
from strategy_01 import Customer, LineItem, Order
import strategy_01

if __name__ == '__main__':
    joe = Customer('John Deo', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem("apple", 10, 1.5),
        LineItem("watermellon", 5, 5.0)
    ]
    fide = strategy_01.FidelityPromo()
    bulk = strategy_01.BulkItemPromo()
    large = strategy_01.LargeOrderPromo()

    print(Order(joe, cart, fide))
    print("------------------\n")

    print(Order(ann, cart, fide))
    print("------------------\n")
    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    print(Order(joe, banana_cart, bulk))
    print("------------------\n")

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, large))
    print(Order(joe, cart, large))



