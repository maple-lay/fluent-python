"""
    第六章，策略
    使用类实现“策略”设计模式
"""

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")  # fidelity: 积分


class LineItem:  # 商品信息登记
    """
    商品信息登记
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
        self.__total = sum(product.total() for product in self.cart)
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        return self.__total

    def due(self):
        if self.promotion:
            return self.total()
        else:
            return self.total() - self.promotion.discount(self)

    def __repr__(self):
        return "<Order total: {%.2f}, due:{%.2f}".format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        pass


class FidelityPromo(Promotion):
    """
    积分大于1000的客户提供5%的折扣
    """

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemProo(Promotion):
    """
    为单件产品数量超过20的客户，提供10%的折扣
    """

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quality > 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    """为商品种类等于或超过10个的用户，提供7%的折扣"""

    def discount(self, order):
        product_kind = {item.product for item in order.cart}
        if len(product_kind) >= 10:
            return order.total() * .07
        else:
            return 0
