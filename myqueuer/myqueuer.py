import rq
import redis
from requests import post
from flask import Flask, request
from redis import Redis
from rq import Queue
import time

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
q = Queue(connection=Redis())

'''def get_hit_count():
    retries = 5
    while True:
        try:
            result = request.form #q.enqueue(request.form)
            job=queue.enqueue(post('http://172.18.0.3/',data = data))
            print(result)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
'''
@app.route('/', methods=['POST'])
def hello():
    result = request.form #q.enqueue(request.form)
    post('http://10.5.0.5/',data = result)#job=queue.enqueue(post('http://172.18.0.2/',data = data))
    print('relay')
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)




	
