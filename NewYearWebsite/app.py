from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route('/')
def isNewYear():
    date = datetime.datetime.now()
    newYear = date.month == 1 and date.day == 1
    newYear = True
    return render_template('index.html', newYear=newYear)

if __name__ == "__main__":
    app.run(debug=True)