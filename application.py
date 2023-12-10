from flask import Flask, render_template

application = app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

# Route for the attendance page
@app.route('/attendancePage')
def attendance_page():
    return render_template('attendancePage.html')

# Route for the admin dashboard
@app.route('/Dashboard')
def dashboard():
    return render_template('Dashboard.html')

# Route for the admin dashboard
@app.route('/report')
def report():
    return render_template('report.html')

# Route for the Employee Home page
@app.route('/Emphome')
def emp_home():
    return render_template('Emp_home.html')

# Route for the Employee Profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Route for the Admin Report page
@app.route('/Adminreport')
def admin_report():
    return render_template('Adminreport.html')

# Route for the Admin Panel page
@app.route('/AdminPanel')
def admin_panel():
    return render_template('AdminPanel.html')

# Route for the Admin Setting page
@app.route('/adminSetting')
def admin_setting():
    return render_template('adminSetting.html')


if __name__ == '__main__':
    app.run(port=8009)
