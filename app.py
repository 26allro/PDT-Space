from flask import Flask 

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/projects')
def projects():
    return flask.render_template('projects.html')

@app.route('/project-details')
def project_details():
    return flask.render_template('project-details.html')

@app.route('/cost-estimator')
def cost_estimator():
    return flask.render_template('cost-estimator.html')

@app.route('/sustainability')
def sustainability():
    return flask.render_template('sustainability.html')

@app.route('/ai-assistant')
def ai_assistant():
    return flask.render_template('ai-assistant.html')

@app.route('/about')
def about():
    return flask.render_template('about.html') 

if __name__ == '__main__':
    app.run()