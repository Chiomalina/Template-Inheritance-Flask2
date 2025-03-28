from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html")

@app.route("/projects", methods=["GET", "POST"])
def projects():
	return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
	return render_template("contact.html", )

@app.route("/blog", methods=["GET", "POST"])
def blog():
	return render_template("blog.html")

@app.route("/shop", methods=["GET", "POST"])
def shop():
	return render_template("shop.html")



if __name__ == "__main__":
	app.run(debug=True, port=5001)