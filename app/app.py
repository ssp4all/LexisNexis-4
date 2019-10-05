from flask import Flask, render_template, url_for, request, json

app = Flask(__name__)

posts = [
    {
        'Crime': 'Alcohol',
        'State': 'NC'
    },
    {
        'Crime': 'Felony',
        'State': 'CA'
    }
]


@app.route("/")
def index():
    return render_template('index.html', posts=posts)

@app.route("/", methods=['POST', 'GET'])
def fetch():
    crime = request.form['crime']
    state = request.form['state']
    
    return tuple([crime, state])
    # print(crime, state)


if __name__ == '__main__':
    app.run(debug=True)
