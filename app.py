from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'salary':'10,00,000',
        'location':'Bangalore, India',
        'image':'static\data_anya.jpg'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'salary':'15,00,000',
        'location':'Delhi, India',
        'image':'static\data_sci.jpg'
    },
    {
        'id':3,
        'title':'AI Intern',
        'salary':'10,00,000',
        'location':'Pune, India',
        'image':'static\ai.jpg'
    },
    {
        'id':4,
        'title':'Front End Developer',
        'salary':'20,00,000',
        'location':'Bangalore, India',
        'image':'static\front_end.jpg'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

