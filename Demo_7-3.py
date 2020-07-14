"""
使用装饰器，优化“策略”模型
"""

promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


# 定义三个折扣函数，计算不同采购订单的折扣
@promotion
def fidelity_promo(order):
    """
    为积分1000或以上的顾客提供5%的折扣
    :param order: Order类的实例
    :return: 优惠的金额
    """
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
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


@promotion
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


def best_promo(order):
    global promos
    return max(promo(order) for promo in promos)
