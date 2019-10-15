from flask import Flask, render_template, url_for, request, json, session, redirect

app = Flask(__name__)

# posts = [
#     {
#         'Crime': 'Alcohol',
#         'State': 'NC'
#     },
#     {
#         'Crime': 'Felony',
#         'State': 'CA'
#     }
# ]

def compar(state, crime):
    with open('combine.json', 'r') as f :
        data = json.load(f)
        lst = data["final"]
        for each_state in lst:
            if list(each_state.keys())[0] == state:
                all_id = list(each_state.values())[0]
                for eachid in all_id:
                    if eachid[0] == crime:
                        sp = eachid[1]
                        return sp
        
    return "Not Found"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST', 'GET'])
def fetch():
    result = []
    crime = request.form['crime']
    state = request.form['state']
    print(state)
    try:
        state = list(state.split(', '))
    except  ValueError:
        pass
    # print(state)
    for i in state:
        print(i)
        result.append(compar(i, crime))
        
    print(result)
    session['result'] = result
    
    if result == []:
        return "Not Found"
    
    return redirect(url_for('output'))

@app.route("/ouput")
def output():
    result = session.get('result', None)
    return render_template('output.html', result=result)
    
if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)
