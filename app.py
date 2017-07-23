from flask import Flask,render_template,request
import random
app= Flask(__name__)

# table=db["odai_user"]
# #Insert a new record.

# # db=dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4")






# print(db.tables)
#  #print(table.columns)
# # for user in table:
# # 	print("Id : "+str(user["id"])+";Name : "+user["name"])


@app.route("/")
def load_page():
	# return render_template("index1.html")
	fortiune=["odai","ashraf","ibrahem","almasri"]
	return render_template ("home.html",wecode=random.choice(fortiune))
@app.route("/aboutme")
def about_me():
	return render_template ("aboutme.html")
	

@app.route("/contact")
def cantact():
	return render_template ("contact.html")


@app.route("/form_response", methods=["POST"])
def form_res():
	user_firstname = request.form["firstname"]
	user_lastname = request.form["lastname"]
	user_message = request.form["message"]
	user_gender = request.form["gender"]
	#return render_template("home.html")
	# table=db["odai_contact"]
	# table.insert(dict(name=user_firstname ,userlastname=user_lastname,usermassege=	user_message,usergender=user_gender))
	# return table
	# return user_firstname +" "+ user_lastname +" "+user_message+" "+user_gender
	# for user in table:
	#  	print("Id : "+str(user["id"])+";Name : "+user["name"])

	# return table.find_one(firstname="firstname")

	return render_template ("formdata.html",thefirstname=user_firstname,thelastname=user_lastname,
		themessage=user_message,thegender=user_gender)
	# return user_firstname + " " + user_lastname + " " + user_message+" "+ user_gender





if __name__=="__main__":
	app.run()