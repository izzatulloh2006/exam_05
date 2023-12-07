import time
#
from celery import Celery

app1 = Celery('hello', broker='pyamqp://quest@localhost/')


@app1.task
def hello():
    print("hello start")
    time.sleep(20)
    return 'hello word'




# @app.task
# def hello():
#     time.sleep(20)
#     return 'hello world'
#
# @app.task
# def function1():
#     time.sleep(10)
#
# @app.task
# def function1():
#     print("function1 started")
#     time.sleep(10)
#     return 'function1 funish'
#
# @app.task
# def function2():
#     print("function2 started")
#     time.sleep(10)
#     return 'function2 funish'




