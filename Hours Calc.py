#Hours Calc
import math
loop1 = True
while loop1:
    print("Hello")
    print("This is the hours calculator")


    loop = True
    while loop:
        total = 0 
        A = int(input("how many days did they work?: "))
        for i in range(1,A+1):
            startinp1 = float(input("What time did they start on day " + str(i) + "?: "))
            finishinp1 = float(input("What time did they finish on day " + str(i) + "?: "))

            startmins = (startinp1 - (math.floor(startinp1))) * 100
            starthours = math.floor(startinp1)
            allstartmins = (starthours * 60) + startmins
            finishmins = (finishinp1 - (math.floor(finishinp1))) * 100
            finishhours = math.floor(finishinp1)
            allfinishmins = (finishhours * 60) + finishmins
            diff = allfinishmins - allstartmins

            if diff > 360:
                diff = diff - 20

            diff = (diff / 60)
            diff = round(diff, 2)
            total = diff + total
        print("they worked",total,"hours")
        repeat = int(input("if you want to use this program again please type '0':"))
        if repeat == 0:
            A = 0
            total = 0
            loop = True
        else:
            loop = False
            loop1 = False

# Made And Designed By Samuel Ol
