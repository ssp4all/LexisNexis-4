from flask import Flask, render_template, url_for
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



if __name__ == '__main__':
    app.run(debug=True)
