from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart(request):
    return render(request, "cart.html", {})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        
        # Save to session
        cart.add(product=product)
        
        # Get cart quantity
        cart_quantity = cart.__len__()
        
        # return response
        response = JsonResponse({'Qty: ': cart_quantity})
        # response = JsonResponse({'Product Name: ': product.name})
        return response
                
                
def cart_delete(request):
    pass
def cart_update(request):
    pass

