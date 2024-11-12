# Nếu trong mật khẩu MySQL có chưa ký tự đặcbiệt, ta có thể làm như sau:
# from urllib.parse import quote
# ...
# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:%s@localhost/saledb' % quote('Admin@123')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:lam27072004Aa@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)