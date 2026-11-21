def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print(add_item("Tea"), add_item("Vada"))


def bill(amount, gst_rate=0.05):
    gst = amount * gst_rate
    total = amount + gst
    return total, gst

total, gst = bill(200)


count = 0

def increment():
    global count
    count += 1

def outer():
    value = 10
    def inner():
        nonlocal value
        value += 1
    inner()
    return value
