from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import requests
import smtplib
import os

app = Flask(__name__)
mail = Mail(app)

EMAIL = 'garrettcodetesting@gmail.com'
PASSWORD = os.environ.get('EMAIL_PASSWORD')
receiver = "swensongarrett@gmail.com"
print(PASSWORD)

def send_contact_form(name, email, number, message):
    try:
        email_message = f'Name {name} \nEmail {email} \nNumber {number} \nMessage {message}'
        print(email_message)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(EMAIL, receiver, email_message)
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")




@app.route('/')
def home():
    return render_template("index.html")


@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        data = request.form
        name = data["name"]
        email=data['email']
        phone=data['phone']
        message=data['message']
        print(name, email, phone, message)
        send_contact_form(name, email, phone, message)
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)

