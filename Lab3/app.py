from flask import Flask, request, redirect, url_for, render_template, request
from flask import session as login_session
from database import query_all,add_cort,query_cart,re_id

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
app.config['SECRET_KEY'] = 'super-secret-key'

##### Code here ######
number=0
@app.route('/')
def homepa():
	return render_template("home.html")
@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/store')
def store():
	products=query_all()
	name=products[0].name
	price=products[0].price
	desc=products[0].desc
	pic=products[0].picture
	idp=products[0].id
	return render_template("store.html",name=name,price=price,desc=desc,pic=pic,id=idp)
@app.route('/cart', methods=["GET","POST"])
def cart():
	if request.method=="GET":
		return render_template("cart.html")
#####################
	elif request.method=="POST":
		idp=request.form["bought"]
		add_cort(idp)
		pro=query_cart()
		pron=[]
		for i in pro:
			pron.append(re_id(i.id))

	return render_template("cart.html",pro=pron)




if __name__ == '__main__':
    app.run(debug=True)