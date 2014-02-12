from flask import Flask, render_template, request, flash
from forms import ContactForm, Unsubscribe
from flask_mail import Mail, Message
import dataset

mail = Mail()

app = Flask(__name__)

app.secret_key = '9sef7s98fe79se8f7s9e8f98fh7fgj98f'

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465 
app.config["MAIL_USE_SSL"] = True 
app.config["MAIL_USERNAME"] = 'your@gmail.com'
app.config["MAIL_PASSWORD"] = 'yourpassword'

mail.init_app(app)

db = dataset.connect('sqlite:///site.db')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required. ')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='yoursending_email@gmail.com', recipients=['email@sentto.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)              
   
            return render_template('contact.html', success=True) 

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    form = Unsubscribe()

    if request.method == 'POST':
        if form.validate() == False:
            flash('Form must be filled out correctly. ')
            return render_template('unsubscribe.html', form=form)
        else:
            table = db['unsub']
            table.insert(dict(unsubscribed=form.email.data))
            return 'You have been unsubscribed.'

    elif request.method == 'GET':
        return render_template('unsubscribe.html', form=form)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

if __name__ == '__main__':
    app.run(debug=True)

