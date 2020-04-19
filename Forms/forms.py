from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dataSubmission.html')

@app.route('/formsSubmission', methods=['post'])
def content():
    name = request.form.get('name')
    return render_template('content.html',name=name)


if __name__ == "__main__":
    app.run(debug=True)