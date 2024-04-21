import random

from ..models import Product


async def get_random_product():
    all_products = Product.objects.all()
    if all_products:
        random_product = random.choice(all_products)
        return random_product
    else:
        return None
