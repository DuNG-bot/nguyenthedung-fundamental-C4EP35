from flask import Flask, render_template

app = Flask(__name__)
profile = {
        "huy": {
            "name":"Nguyen Quang Huy",
            "age":29,
            "gender":"Male",
            "hobbies":['Basketball','Fishing','Dancing'],
            "pic":"http://www.elle.vn/wp-content/uploads/2014/11/03/ellevn-quang-huy-1.jpg"
        },
        "tuananh": {
            "name":"Huynh Tuan Anh",
            "age":22,
            "gender":"Male",
            "hobbies":['Guitar','Singing','Running'],
            "pic":"https://nguoinoitieng.tv/images/nnt/99/0/bdzh.jpg"
        },
    }
@app.route('/user/<username>')
def people(username):
    if username not in profile:
        return "User not found!!"
    
    user = profile[username]
    return render_template('user.html',NAME=user)

@app.route('/user')
def home_page():
    return 'OUR PROSPECTIVE MEMBERS'




if __name__ == "__main__":
    app.run(debug=True)