from time import *
import random as r

def mistake(test_1,test_2):

    error=0
    for i in range(len(test_1)):
        try:
            if test_1[i]!=test_2[i]:
                error = error+1
        except:
            error=error+1
    return error
def speed_time(time_s,time_e,test2):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(test2)/time_R
    return round(speed)


test=["Twinkle Twinkle little star","how i wonder what you are","up above the world so high","like a dimond in the sky"]
test1=r.choice(test)
print("#############TYPING SPEED CALCULATOR############")
print(test1)
print()
time_1=time()
test2=input("Here you can enter your word: ")
time_2=time()
print('speed:',speed_time(time_1,time_2,test2),"w/sec")
print("ERROR:",mistake(test1 ,test2))


