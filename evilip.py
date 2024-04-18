#Please use this tool ethicly ;) and this tool may not find every single ip
#so dont rely on it
print("Loading...")
print()
import random
def evilip():
    randomipstart = random.randint(0, 3)
    if randomipstart == 0:
        startip = "0"
    elif randomipstart == 1:
        startip = "192"
    elif randomipstart == 2:
        startip = "255"
    elif randomipstart == 3:
        startip = "172"
    else:
        pass
    
    randomsecondip = random.randint(0, 6)
    if randomsecondip == 0:
        secondip = "158"
    elif randomsecondip == 1:
        secondip = "168"
    elif randomsecondip == 2:
        secondip = "0"
    elif randomsecondip == 3:
        secondip = "43"
    elif randomsecondip == 4:
        secondip = "24"
    elif randomsecondip == 5:
        secondip = "27"
    elif randomsecondip == 6:
        secondip = "30"
    else:
        pass
    
    randomthirdip = random.randint(0, 3)
    if randomthirdip == 0:
        thirdip = "0"
    elif randomthirdip == 1:
        thirdip = "42"
    elif randomthirdip == 2:
        thirdip = "1"
    elif randomthirdip == 3:
        thirdip = "255"
    else:
        pass
    
    randomforthip = random.randint(0, 3)
    if randomforthip == 0:
        forthip = "0"
    elif randomforthip == 1:
        forthip = "1"
    elif randomforthip == 2:
        forthip = "255"
    elif randomforthip == 3:
        forthip = "24"
    else:
        pass
    
    finalip = startip+"."+secondip+"."+thirdip+"."+forthip
    print(finalip)

def randombruhgo():
    randomgobruhip1 = str(random.randint(0, 255))
    randomgobruhip2 = str(random.randint(0, 255))
    randomgobruhip3 = str(random.randint(0, 255))
    randomgobruhip4 = str(random.randint(0, 255))
    randomgobruhall = randomgobruhip1+"."+randomgobruhip2+"."+randomgobruhip3+"."+randomgobruhip4
    print(randomgobruhall)



def waysy():
    numberofips = int(input("How many random IPs should I generate? : "))
    for i in range(numberofips):
        evilip()  

def waysy2():
    randomgobruhchoose = int(input("And how many do you exactly want?: "))
    for p in range(randomgobruhchoose):
        randombruhgo()

print("Loading Successful!")
print()
print("Would like it to be the proper way (y) or the random go way (y2)?: ")
ways = input()
if ways == "y":
    waysy()
else:
    waysy2()