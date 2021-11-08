from flask_app import app, render_template, request, redirect, session
from flask_app.models.model_email import Email

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create_email():
    data = {
        "email_address" : request.form['email_address']
    }

    if not Email.validate_email(request.form):
        return redirect('/')

    Email.save(data)
    return redirect('/results')

@app.route('/results')
def show_emails():
    return render_template("results.html", emails=Email.get_all())