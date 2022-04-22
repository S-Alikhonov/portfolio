from flask import Flask, render_template
from data import my_projects,bio

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html',bio=bio)

@app.route('/projects')
def projects():
    return render_template('projects.html',projects=my_projects)


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    app.run(debug=True)


    