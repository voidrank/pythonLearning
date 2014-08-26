from flask import Flask
app = Flask(__name__)

@app.route("/user/<username>")
def show_user_profile(username):
	return username

@app.route("/post/<int:post_id>")
def show_post(post_id):
	return "post_id = %d" % post_id

if __name__ == "__main__":
	app.debug = 1
	app.run()
