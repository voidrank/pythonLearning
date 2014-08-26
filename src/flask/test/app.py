from flask import *
import pymongo
import os

app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
def index():
	if "register" in request.form:
		return redirect(url_for("register"))
	elif "login" in request.form:
		return redirect(url_for("login"))
	elif "blog" in request.form:
		return redirect(url_for("blog"))
	else:
		if "logout" in request.form:
			session.pop("username", None)
		return render_template("index.html", session=session)

@app.route("/login", methods=["GET", "POST"])
def login():
	if "username" in request.form:
		conn = pymongo.Connection("localhost", 27017)
		col = conn.sMyBlog.User
		if (col.find_one({
				"username": request.form["username"],
				"password": request.form["password"]
			})):
			session["username"] = request.form["username"]
			flash("Login successfully")
			return redirect(url_for("index"))
		else:
			return "wrong username or password"
	else:
		return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":
		conn = pymongo.Connection("localhost", 27017)
		col = conn.sMyBlog.User
		if (col.find_one({"username":request.form["username"]})):
			return render_template("register.html")
		else:
			col.insert({
				"username" : request.form["username"],
				"password" : request.form["password"]
			})
			return "register successfully"
	else:
		return render_template("register.html")

@app.route("/blog", methods=["GET", "POST"])
def blog():
	if "username" in session:
		conn = pymongo.Connection("localhost", 27017)
		col = conn.sMyBlog.blog
		if "Write new blog" in request.form:
			return redirect(url_for("newblog"))
		else:
			return render_template(
				"blog.html", 
				bloglist=col.find({
					"username" : session["username"]
					})[0:20]
				)
	else:
		return render_template("unlogged.html")

@app.route("/blog/new", methods=["GET", "POST"])
def newblog():
	if "username" in session:
		conn = pymongo.Connection("localhost", 27017)
		col = conn.sMyBlog.blog
		if "text" in request.form:
			col.insert({
					"username" : session["username"],
					"title" : request.form["title"],
					"text" : request.form["text"]
				})
			return redirect(url_for("blog"))
		else:
			return render_template("newblog.html")
	else:
		return render_template("unlogged.html")


app.secret_key = os.urandom(24)

if __name__ == "__main__":
	app.debug = 1
	app.run()