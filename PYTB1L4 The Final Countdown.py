import time 

nummer = 1000

while nummer <= 1000:
    print(nummer)
    nummer = nummer -1
    time.sleep(1)
    
    if nummer == 0:
        print("Dit is speciaal :) ")
