import pyrebase
from email_config import add_data,send_email_to
from configruation import config
firebase = pyrebase.initialize_app(config)
db =firebase.database()


def stream_handler(message):
    print(message["event"]) #prints the method used
    print(message["path"]) #prints the path where data is inserted
    print(message["data"])
    value= message["data"]
    if len(value)>2:
    	pass
    else:
        add_data(value)
        a=value['Name']
        b=value['Email']
        send_email_to(a,b)
	



my_stream = db.child("users").stream(stream_handler)
	
