from flask import Flask,render_template,request
import random



app= Flask(__name__)

@app.route("/")
def load_page():
	#return render_template("index.html")
	fortiune=["odai","ashraf","ibrahem","almasri"]
	return render_template ("home.html",wecode=random.choice(fortiune))
@app.route("/aboutme")
def about_me():
	return render_template ("aboutme.html")
	


@app.route("/contact")
def cantact():
	return render_template ("contact.html")



@app.route("/form/")
def form():
	return render_template ("input_form.html")
@app.route("/form_response", methods=["POST"])
def form_res():
	user_firstname = request.form["firstname"]
	user_lastname = request.form["lastname"]
	user_message = request.form["message"]
	user_gender = request.form["gender"]
	return user_firstname +" "+ user_lastname +" "+user_message+" "+user_gender
	return render_template ("form data.html",thefirstname=user_firstname,thelastname=user_lasttname,
		themessage=user_message,thegender=user_gender)





if __name__=="__main__":
	app.run(port=5050)