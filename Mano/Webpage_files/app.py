from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
# import requests

# Create an instance of Flask
app = Flask(__name__,template_folder='templates')


model=
# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    return render_template("index.html")  

# Route to the basic info
@app.route("/basic_info")
def basic_info():
    print("================")
    print("Basic Info")
    print("================")
    
    return render_template("index.html") 

# Route to the basic info
@app.route("/new_index.html")
def new_index():
    print("================")
    print("new_index")
    print("================")
    
    return render_template("new_index.html") 

# Route to the basic info
@app.route("/matchme", methods=["POST"])
def matchme():
    print("================")
    print("Match me")
    print("================")

    age=request.form["Age"]
    print(age)
    sex=request.form["Sex"]
    print(sex)
    income=request.form["Income"]
    print(income)
    status=request.form["Status"]
    print(status)
    diet=request.form["Diet"]
    print(diet)
    education=request.form["Education"]
    print(education)
    job=request.form["Job"]
    print(job)
    orientation=request.form["Orientation"]
    print(orientation)
    religion=request.form["Religion"]
    print(religion)
    height=request.form["Height"]
    print(height)
    ethnicity=request.form["Ethnicity"]
    print(ethnicity)
    bodytype=request.form["Bodytype"]
    print(bodytype)
    input_df = pd.DataFrame({"age_scaled": age })

    predications=model.predict(input_df)
     output = round(prediction[0], 2)

    return render_template("new_index.html") 

if __name__ == "__main__":
    app.run(debug=True)


