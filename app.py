from flask import Flask,render_template
import random



app= Flask(__name__)

@app.route("/")
def load_page():
	#return render_template("index.html")
	fortiune=["odai","ashraf","ibrahem","almasri"]
	return render_template ("index.html",wecode=random.choice(fortiune))
@app.route("/aboutme")
def about_me():
	return render_template ("index1.html")
	


@app.route("/contact")
def cantact():
	return render_template ("contact.html")





if __name__=="__main__":
	app.run(port=5050)