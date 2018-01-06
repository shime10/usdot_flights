from flask import Flask, render_template
app = Flask(__name__)

HOST = 'localhost'
PORT = 4900

@app.route('/')
def home():

	return render_template('airports.html')

if __name__ == '__main__':
	app.run(debug=True, host=HOST, port=PORT)
