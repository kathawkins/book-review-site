from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/review_eloquent-ruby") 
def a_review():
	return render_template('eloquent-ruby.html')

@app.route("/contact") 
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
    app.run()