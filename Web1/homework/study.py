from flask import Flask,render_template,redirect

app = Flask(__name__)

Dung = {
    "Full_name":"NGUYEN THE DUNG",
    "Employment":"College student",
    "School":"Life",
    "Hobbies": ["Games","Music","Sleeping"],
    "Dog_name":"Imaginary",
    "Crush":"Missing"
}

@app.route("/about-me")
def me():
    return render_template("Dung.html",Me=Dung)

@app.route("/school")
def Mindx():
    return redirect('http://techkids.vn')

if __name__ == "__main__":
    app.run(debug=True)