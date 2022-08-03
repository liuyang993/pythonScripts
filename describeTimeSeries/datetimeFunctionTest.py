import datetime
import time

x = datetime.datetime(2022,7,25,9,0,2)
print(x)
print(x.time())


# current_time = x.strftime("%H:%M:%S")
# print(current_time)


while True:
    # print(x.time())
    if (x.time() >  datetime.time(9,1)) and (x.time() <  datetime.time(9,2)):
        print('market stop')
        x= x + datetime.timedelta(seconds=1)
        continue
    print('market trade')

    time.sleep(0.1)
    x= x + datetime.timedelta(seconds=1)


    # if (x.time() >  datetime.time(10,15)) and (x.time() <  datetime.time(10,30)):
    #     x= x + datetime.timedelta(seconds=1)
    #     continue

    # if (x.time() >  datetime.time(11,30)) and (x.time() <  datetime.time(13,30)):
    #     x= x + datetime.timedelta(seconds=1)
    #     continue
    