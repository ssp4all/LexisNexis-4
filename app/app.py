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
def compar(state, crime):
    with open('combine.json', 'r') as f:
        data = json.load(f)
        lst = data["final"]
        for each_state in lst:
            if list(each_state.keys())[0] == state:
                all_id = list(each_state.values())[0]
                for eachid in all_id:
                    if eachid[0] == crime:
                        sp = eachid[1]
                        return sp
        
    return ""

@app.route("/")
def index():
    return render_template('index.html', posts=posts)

@app.route("/", methods=['POST', 'GET'])

    
def fetch():
    crime = request.form['crime']
    state = request.form['state']
    ans = compar(state, crime)
    if ans == "":
        return "Not Found"
    
    return ans
    # print(crime, state)


if __name__ == '__main__':
    app.run(debug=True)
