from flask import Flask
from flask.helpers import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/user/')
def show_profile():
    return 'User Page'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User: %s' % username

@app.route('/user/id:<int:post_id>')
def show_post(post_id):
    return 'User id: %d' % post_id

with app.test_request_context():
    url_for('show_user_profile', username="Johny Depp")
if __name__ == '__main__':
    app.debug = True
    app.run()
    # or 
    # app.run(debug=True)
    
    # app.run(host='0.0.0.0') # self comp