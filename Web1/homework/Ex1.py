from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/bmi/<int:weight>/<int:height>')
# def bmi(weight,height):
#     D = weight/((height/100)**2)

#     if D < 16:
#         return("You're severely underweight!!!")
#     elif D < 18.5:
#         return("You're underweight!")
#     elif D < 25:
#         return("You're normal. Keep it up :D")
#     elif D < 30:
#         return("You're overweight. Be mindful of your health!")
#     else:
#         return('Obesity has joined the chat >.<')

@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    D = weight/((height/100)**2)
    return render_template('bmi.html', d=D)

    


if __name__=="__main__":
    app.run(debug=True)