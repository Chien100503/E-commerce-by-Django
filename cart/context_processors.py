from .cart import Cart

# Bộ xữ lý để khi thêm vào giỏ hàng
def cart(request):
    # return the default data from Cart
    return {'cart': Cart(request)}