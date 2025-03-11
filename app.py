from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# import mysql.connector


# Hardcoded credentials for simplicity (you can replace this with a database query)
USERNAME = "admin"
PASSWORD = "password123"

@app.route('/', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password match the hardcoded credentials
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('log_in'))  # Redirect to logout page if login is successful
        else:
            # If credentials are incorrect, show an error message (you can customize this)
            return render_template('login.html', error="Invalid username or password")
    
    # If GET request, just render the login page
    return render_template('login.html')

@app.route('/login')
def log_in():
    
    return '''
        <h1>You are logged in successfully!</h1>
        <form action="/logout" method="POST">
            <button type="submit">Logout</button>
        </form>
    '''

@app.route('/logout', methods=['POST'])
def log_out():
    return "You are logged out successfully"


if __name__ == '__main__':
    app.run(debug=True)
