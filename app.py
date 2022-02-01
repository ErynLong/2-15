from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/students', methods=['GET'])
def students():
    my_students = ['Caleb', 'Kristen', 'Eryn', 'Zak', 'David']
                                            #  Name in Jinja = name in python
    return render_template('students.html.j2', students = my_students)

@app.route('/ergast', methods = ['GET', 'POST'])
def ergast():
    if request.method == 'POST':
        #contact the api and get the info for the year and round from the form
        year = request.form.get('year')
        round = request.form.get('round')
        url = f"http://ergast.com/api/f1/{year}/{round}/driverStandings.json"
        response = requests.get(url)
        if response.ok:
            data = response.json()["MRData"]["StandingsTable"]["StandingsLists"]
            if len(data)<=0:
                print('here')
                error_string = f"There is no info for {year} round {round}"
                return render_template('ergast.html.j2', error = error_string)
            
            all_racers=[]
            for racer in data:
                racer_dict={}
                racer_dict={
                    'first_name':racer['Driver']['givenName'],
                    'last_name':racer['Driver']['familyName'],
                    'position':racer['position'],
                    'wins':racer['wins'],
                    'DOB':racer['Driver']['dateOfBirth'],
                    'nationality':racer['Driver']['nationality'],
                    'constructor':racer['Constructors'][0]['name']
                }
                all_racers.append(racer_dict)
            return render_template('ergast.html.j2', racers = all_racers)
        else:
            error_string = "Houston We Have a Problem"
            return render_template('ergast.html.j2', error = error_string)
    return render_template('ergast.html.j2')