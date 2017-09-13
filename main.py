from gopigo import*
import time 
class Piggy(object):
    def __init__(self):
        print("HelLO, I'm your robot")
        self.dance()

    def dance(self):
        time.sleep(1.5)
        right_rot()
        time.sleep(.5)
        stop()



###### My App

dre = Piggy()