from flask import Flask, render_template, request, redirect, url_for
from salesforceConnection import makeNewUser, validateUser, addResume

app = Flask(__name__)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        resume_text = request.form.get('resume-upload')
        cover_text = request.form.get('cover-upload')
        app_status = "In Progress"
        addResume(resume_text, cover_text, app_status)

        return render_template('dashboard.html', app_status=app_status)
    return render_template('dashboard.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if validateUser(email, password):
            return render_template('dashboard.html')
        else:
            return render_template('index.html')

    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user_type = request.form.get('user_type')

        makeNewUser(first_name, last_name, username, email, password, user_type)

        return redirect(url_for('index'))

    return render_template('createAccount.html')


if __name__ == '__main__':
    app.run(debug=True)
