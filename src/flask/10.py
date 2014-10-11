from flask import Flask
app = Flask(__name__)

def hello_world():
	return "hello_world"
hello_world = app.route("/")(hello_world)

if __name__ == '__main__':
	app.debug = True
	app.run()
	#app.run(debug=True)
