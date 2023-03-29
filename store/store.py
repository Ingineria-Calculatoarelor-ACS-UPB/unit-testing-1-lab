#         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#       ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
#     ░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#     ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
# ░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
#   ▒▒▒▒▒▒░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░▒▒
#     ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
#       ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
#       ▒▒▒▒▒▒░░░░░░░░░░░░▒▒██████░░░░░░░░▒▒
#       ▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░▒▒
#       ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░
#     ░░▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░
#     ▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒  ██
# ░░██  ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒  ██
# ░░██  ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒  ██
# ░░██  ▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒  ██
# ░░██  ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒  ██
# ░░██  ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒  ██
# ░░██  ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒  ██
#       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#             ░░▓▓░░              ░░▓▓░░
#               ██                  ██
#               ██                  ██
#               ██                  ██
#               ████                ██▓▓
###################################################

class Store:
    def __init__(self, name, location, products=[]):
        self.name = name
        self.location = location
        self.products = products

    def add_product(self, product):
        if product.name in [product.name for product in self.products]:
            if product.price in [product.price for product in self.products]:
                raise Exception(product.name + "already exists in " + self.name)

        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    # returns the first alphabetical product found that respect the constraint
    def get_the_most_expensive_product(self):
        return max(self.products, key=lambda product:product.price)

    # returns the first alphabetical product found that respect the constraint
    def get_highest_quantity_products(self):
        return max(self.products, key=lambda product:product.quantity)