from flask import Flask, request
from time import time, sleep

import pymongo

myclient = pymongo.MongoClient("mongodb://user:pwd@10.5.0.3:27017/mydatabase")
mydb = myclient["mydatabase"]
mycol = mydb["messages"]

app = Flask(__name__)
number_list=[]
@app.route('/', methods=['POST'])
def hello(mycol=mycol):
    incoming_dict=request.form
    print(incoming_dict)
    received_time=time()*1000
    number_list.append(incoming_dict)
    
    mydict={'number':incoming_dict['number'],
	'sent_time':incoming_dict['time'],
	'received_time':received_time,
	'latency':received_time-float(incoming_dict['time'])
	} 
    x = mycol.insert_one(mydict)

    #print(request.form) #should display a bunch of numbers
    return my_dict

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
