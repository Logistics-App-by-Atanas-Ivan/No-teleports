# from models.category import Category
# from models.product import Product
# from models.shampoo import Shampoo
# from models.shopping_cart import ShoppingCart
# from models.toothpaste import Toothpaste
# from models.cream import Cream

class ApplicationData:
    def __init__(self):
        self._routes = []
        self._packages =[]
        self._users = []

    
    def user_exists(self, email):
        pass

    def add_package(self, package):
        self._packages.append(package)

    

