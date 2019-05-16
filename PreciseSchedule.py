import sched, time
import datetime
import random




def whileOneSecond():
    startMillSecond = int(time.time() * 1000)
    while True:
        print(datetime.datetime.now())
        f= random.random()/10
        #print(f)
        time.sleep(f)
        millSeondDiff = int(time.time() * 1000) - startMillSecond
        #time.sleep(1)
        time.sleep((1000-millSeondDiff)/1000)
        startMillSecond = int(time.time() * 1000)

""" s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print(time.time())
    #print("Doing stuff...when ",datetime.datetime.now())
    # do your stuff
    s.enter(1, 1, do_something, (sc,))0

s.enter(1, 1, do_something, (s,))
s.run() """

whileOneSecond()