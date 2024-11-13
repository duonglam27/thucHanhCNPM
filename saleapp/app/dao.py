# dao== data access object ( dung de truy van du lieu)
from itertools import product

from app.models import Category,Product

def load_categories():
    return Category.query.order_by('id').all()


def load_products(kw=None):
    products=Product.query.order_by('category_id')

    if kw:
        products=products.filter(Product.name.contains(kw))

    return products.all()