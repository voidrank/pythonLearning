from flask import Flask
app = Flask(__name__)

@app.route("/<fid>")
def hello_world(**arg):
	return str(arg['fid'])

if __name__ == '__main__':
	app.debug = True
	app.run()
	#app.run(debug=True)
