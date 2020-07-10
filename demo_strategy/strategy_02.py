"""
使用函数实现策略模式
"""

from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")


class LineItem:
    """
    记录单间商品的信息
    """

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:
    """
    上下文
    """

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
        self.__total = sum(cart_item.total() for cart_item in self.cart)

    def total(self):
        return self.__total

    def due(self):
        if not self.promotion:
            return self.total()
        else:
            return self.total() - self.promotion(self)

    def __repr__(self):
        return "<Order total:{:.2f}, due:{:.2f}".format(self.total(), self.due())


# 定义三个折扣函数，计算不同采购订单的折扣
def fidelity_promo(order):
    """
    为积分1000或以上的顾客提供5%的折扣
    :param order: Order类的实例
    :return: 优惠的金额
    """
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """
    为单个数量大于或等于20的商品提供10%的折扣
    :param order: Order类的实例
    :return: 优惠的金额
    """
    discount = 0
    for cart_item in order.cart:
        if cart_item.quantity >= 20:
            discount += cart_item.total() * .1
    return discount


def large_order_promo(order):
    """
    订单中不同商品种类大于或等于10种，提供7%的折扣
    :param order: Order类的实例
    :return: 优惠的金额
    """
    cart_kind = {cart_item.product for cart_item in order.cart}
    if len(cart_kind) >= 10:
        return order.total() * .07
    else:
        return 0
