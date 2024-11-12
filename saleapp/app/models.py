from enum import unique
from xml.dom.minidom import Comment

from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship
from app import db, app
from sqlalchemy import Column, Integer, String, Float, column, ForeignKey


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)
    products = relationship('Product', backref='category',
                            lazy=True)  # backref='category' : truyen doi tuong category vao Product,  lazy=True ve phia nhieu


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)  # unique: khong cho phep trùng
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(VARCHAR(255), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():

        # db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Laptop')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        data = [{
            "id": 1,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image": "https://taozinsaigon.com/files_upload/product/06_2022/thumbs/600_iphone_7_plus_mau_hong.jpg",
            "category_id": 1
        }, {
            "id": 2,
            "name": "iPad M1",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://topstore.vn/uploads/ipad_pro_12_1648726951.9_inch_m1_2021.jpg",
            "category_id": 2
        }, {
            "id": 3,
            "name": "IPhone 15",
            "description": "Apple, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://product.hstatic.net/1000063620/product/ip-19e6fb19.jpg",
            "category_id": 1
        }, {
            "id": 4,
            "name": "IPhone 5S",
            "description": "Apple, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://cdn.tgdd.vn/Products/Images/42/60546/iphone-5s-16gb-sliver-750x500.png",
            "category_id": 1
        }, {
            "id": 5,
            "name": "MacBook M1",
            "description": "Apple, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://i0.wp.com/vuatao.vn/wp-content/uploads/2021/06/macbook-air-m1-2020-8-core-gpu-silver-thumb-650x650-1.png?fit=650%2C650&ssl=1",
            "category_id": 3
        }, {
            "id": 6,
            "name": "MacBook M3",
            "description": "Apple, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://bizweb.dktcdn.net/thumb/1024x1024",
            "category_id": 3
        }]
        for p in data:
            prod = Product(name=p['name'], description=p['description'], price=p['price'], image=p['image']
                           , category_id=p['category_id'])
            db.session.add(prod)

        db.session.commit()
