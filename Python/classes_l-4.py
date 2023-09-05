class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=60, brend=''):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно быть 2 символа или более')  
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if  self.discount > self.max_discount:
            self.discount = self.max_discount 
        self.brend = brend.strip()   

    def discounted(self):
        return self.price - self.price * self.discount / 100
    
    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        self.stock -= items_count       

    def __repr__(self):
        return f'<Product name: {self.name}, brend: {self.brend}, price: {self.price}, stock: {self.stock}, discount: {self.discount}, discounted price: {self.discounted()}>'


class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=60, brend=''):
        super().__init__(name, price, stock, discount, max_discount, brend)
        self.color = color

    def __repr__(self):
        return f'<Phone: {self.name}, Brend: {self.brend}, color: {self.color}, price: {self.price}, stock: {self.stock}, Discount: {self.discount}, Discounted price: {self.discounted()}>'
    
My_Phone = Phone('Iphone RS 200', 450, "red", stock=60, discount=30)
My_Phone.sell(10)
print(My_Phone)  

class Sofa(Product):
    def __init__(self, name, price, color, textture, stock=0, discount=0, max_discount=60, brend=''):
        super().__init__(name, price, stock, discount, max_discount, brend)
        self.color = color
        self.texture = textture

    def __repr__(self):
        return f'<Sofa: {self.name}, Brend: {self.brend}, color: {self.color}, fabric material: {self.texture}, price: {self.price}, stock: {self.stock}, Discount: {self.discount}, Discounted price: {self.discounted()}>'
    

My_sofa = Sofa('Virginia', 600, 'blue', 'Genuine Leather', discount=40) 
print(My_sofa) 
print(My_sofa.color)  
