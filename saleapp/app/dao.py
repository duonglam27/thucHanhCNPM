# dao== data access object ( dung de truy van du lieu)
from itertools import product

from app.models import Category,Product

def load_categories():
    return Category.query.order_by('id').all()


def load_products(kw=None,cate_id=None,page=1):

    query=Product.query

    if kw:
        query=query.filter(Product.name.contains(kw))
    if cate_id:
        query=query.filter(Product.category_id==cate_id)
    return query.all()