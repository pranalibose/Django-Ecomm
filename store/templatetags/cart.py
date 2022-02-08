from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    keys = cart.keys()
    if keys:
        for id in keys:
            if int(id)==product.id:
                return True

    return False

@register.filter(name='cart_quantity')
def cart_quantity(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)

    return 0

@register.filter(name='price_total')
def price_total(product , cart):
    return product.price * cart_quantity(product, cart)


@register.filter(name='total_cart_price')
def total_cart_price(product, cart):
    sum = 0
    for p in product:
        sum += price_total(p, cart)
    return sum

@register.filter(name='cart_quantity_sum')
def cart_quantity_sum(product , cart):
    keys = cart.keys()
    quantity_sum = int(0)
    for id in keys:
        quantity_sum = quantity_sum + cart.get(id)

    return quantity_sum