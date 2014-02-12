from flask.ext.wtf import Form

from wtforms import TextField, BooleanField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name. ")])
    email = TextField("Email", [validators.Required("Please enter your email address. "), validators.Email("Please enter your email address. ")])
    subject = TextField("Subject", [validators.Required("Please enter a subject. ")])
    message = TextAreaField("Message", [validators.Required("Please enter a message. ")])
    submit = SubmitField("Send")

class Unsubscribe(Form):
    email = TextField("Email", [validators.Required("You must enter your email address. "), validators.Email("You must enter a valid email address.")])
    submit = SubmitField("Unsubscribe")


