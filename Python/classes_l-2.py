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

product1 = Product('Phone R-300', 300, stock=40, discount=35, brend='Toshiba')  
print(product1)
product1.sell(5)
print(product1)




