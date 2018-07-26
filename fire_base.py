"""run this file to enter the data into users node"""
import pyrebase
from configruation import config


firebase1 = pyrebase.initialize_app(config)
db1 =firebase1.database()


while True:
	d={}
	x=str(input("enter username : "))
	y=str(input("Enter E-mail : "))
	d['Name']=x
	d['Email']=y
	db1.child('users').push(d)
