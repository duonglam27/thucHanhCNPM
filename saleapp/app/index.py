from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    cates=dao.load_categories()

    cate_id=request.args.get('category_id')
    page=request.args.get('page',1)
    kw=request.args.get('kw')
    prods=dao.load_products(kw=kw,cate_id=cate_id,page=int(page))
    return render_template('index.html', categories=cates, products=prods)

if __name__=='__main__':
    app.run(debug=True)
