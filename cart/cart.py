class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # get the current session key if it exits
        cart =  self.session.get('session_key')
        
        # If the user new, no session key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        # make sure cart is available on all pages of the size
        self.cart = cart 
        
    def add(self, product):
        product_id = str(product.id)
        
        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
            
        self.session.modified = True
    def __len__(self):
        return len(self.cart) 