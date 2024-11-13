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
            "image": "https://product.hstatic.net/1000063620/product/ip-15-pro-max-mhm-xanh_8dc67ad091eb477099276543f9e6fb19.jpg",
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
            "image": "https://hieuapple.com/uploads/shops/2021_04/macbook-pro-mpxq2.3.jpg",
            "category_id": 3
        }, {
            "id": 6,
            "name": "MacBook M3",
            "description": "Apple, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://macone.vn/wp-content/uploads/2023/11/mbp14-m3-max-pro-spaceblack-gallery2-202310-lon-1024x787.jpeg",
            "category_id": 3
        }, {
            "id": 7,
            "name": "SamSung S21",
            "description": "Apple, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbGswIwdezd6Y6Z1lmNgIys0bAuiipSBnjNA&s",
            "category_id": 1
        }, {
            "id": 8,
            "name": "SamSung S25",
            "description": "Apple, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://didongmoi.com.vn/upload/images/product/samsung-galaxy-s25-ultra-gia-re-3-2.jpg",
            "category_id": 1
        }, {
            "id": 9,
            "name": "Lenovo ThinkPad X1 ",
            "description": "Apple, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://product.hstatic.net/1000331874/product/thinkpad_x1_nano_gen_1_31b3ed9664994178a888eadd06c0b029.jpg",
            "category_id": 3
        }, {
            "id": 10,
            "name": "Dell XPS",
            "description": "Apple, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://thegioiso365.vn/wp-content/uploads/2021/01/dell-xps-13-9380-4-1602066716.jpg",
            "category_id": 3
        }]

        for p in data:
            prod = Product(name=p['name'], description=p['description'], price=p['price'], image=p['image']
                           , category_id=p['category_id'])
            db.session.add(prod)

        db.session.commit()
