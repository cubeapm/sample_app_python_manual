import os
import time
def someTask():
    childTask(2)
    try:
        errorTask()
    except Exception as ex:
        pass
    try:
        errorTaskWithSpan()
    except:
        pass

    time.sleep(0.1)

def childTask(val):
    pass

def errorTask():
    raise KeyError()

def errorTaskWithSpan():
    raise KeyError()

if __name__ == "__main__":
    for i in range(2):
        someTask()
        time.sleep(1)
