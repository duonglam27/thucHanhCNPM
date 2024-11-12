# dao== data access object ( dung de truy van du lieu)
def load_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Laptop"
    }
    ]


def load_product():
    return [{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":"https://taozinsaigon.com/files_upload/product/06_2022/thumbs/600_iphone_7_plus_mau_hong.jpg",
        "category_id": 1
    }, {
        "id": 2,
        "name": "iPad M1",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":"https://topstore.vn/uploads/ipad_pro_12_1648726951.9_inch_m1_2021.jpg",
        "category_id": 2
    }, {
        "id": 3,
        "name": "IPhone 15",
        "description": "Apple, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":"https://product.hstatic.net/1000063620/product/ip-15-pro-max-mhm-xanh_8dc67ad091eb477099276543f9e6fb19.jpg",
        "category_id": 1
    }, {
        "id": 4,
        "name": "IPhone 5S",
        "description": "Apple, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":"https://cdn.tgdd.vn/Products/Images/42/60546/iphone-5s-16gb-sliver-750x500.png",
        "category_id": 1
    }, {
        "id": 5,
        "name": "MacBook M1",
        "description": "Apple, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":"https://i0.wp.com/vuatao.vn/wp-content/uploads/2021/06/macbook-air-m1-2020-8-core-gpu-silver-thumb-650x650-1.png?fit=650%2C650&ssl=1",
        "category_id": 3
    }, {
        "id": 6,
        "name": "MacBook M3",
        "description": "Apple, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":"https://bizweb.dktcdn.net/thumb/1024x1024/100/318/659/products/mbp14-spacegray-gallery1-202310-copy-3ff6d264-4004-4e17-ae1b-0fd63e5061a1.jpg?v=1710587071927",
        "category_id": 3
    }]
