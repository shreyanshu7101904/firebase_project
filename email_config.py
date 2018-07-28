
import smtplib
import pyrebase
from configruation import config,userId,Password


def add_data(value):
	'''Function to insert values in diffrent node from existing node users'''
	firebase1 = pyrebase.initialize_app(config)
	db1 =firebase1.database()
	db1.child("userInformation").push(value)


def send_email_to(username,input_id):
	'''function to send email to user'''
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(userId, Password)
	message = "Dear "+username+", Welcome to our app"
	s.sendmail(userId,input_id , message)
	s.quit()

