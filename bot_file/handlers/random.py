import random

from ..models import Product


async def get_random_product():
    # Получаем все продукты из базы данных
    all_products = Product.objects.all()
    # Если есть хотя бы один продукт в базе данных
    if all_products:
        random_product = random.choice(all_products)
        return random_product
    else:
        return None
