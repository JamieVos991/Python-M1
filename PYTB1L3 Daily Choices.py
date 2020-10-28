
import time

print("")
print("Hey, dit is een spel waarbij je keuzes moet maken! Je beantwoord de vragen door A of B te typen. ")
print("")

def Vraag1():
    print("")
    vraag1 = input("Stel, je mist de bus. Ga je wachten voor de volgende bus over 60 minuten of alvast lopen naar huis (5 Kilometer) ")

    if vraag1 == "A" or vraag1 == "a":
        print("")
        print("Lui...")
        Vraag2()

    elif vraag1 == "B" or vraag1 == "b":
        print("")
        print("Zozo...")
        Vraag2()

    else:
        print("")
        print("Niks ingevuld")
        time.sleep(1)
        Vraag1 

def Vraag2():
    print("")
    vraag2 = input("Tandpasta gemaakt van chilipepers OF … toiletpapier van schuurpapier? ")
                   
    if vraag2 == "A" or vraag2 == "a":
        print("")
        print("Das heet 0_o")
        Vraag3()

    elif vraag2 == "B" or vraag2 == "b":
        print("")
        print("xD...")
        Vraag3()

    else:
        print("")
        print("Niks ingevuld")
        time.sleep(1)
        Vraag2()

def Vraag3():
    print("")
    vraag3 = input("Kies je een extra been OF … een derde arm? ")

    if vraag3 == "A" or vraag3 == "a":
        print("")
        print("Dat wordt opnieuw leren lopen...")
        Vraag4()

    elif vraag3 == "B" or vraag3 == "b":
        print("")
        print("Die kan je handig gebruiken!")
        Vraag4()
    
    else:
        print("")
        print("Niks ingevuld")
        time.sleep(1)
        Vraag3()

def Vraag4():
    print("")
    vraag4 = input("Doe je vandaag één wens OF … wacht je liever tien jaar om er dan drie te mogen maken? ")

    if vraag4 == "A" or vraag4 == "a":
        print("")
        print("Vrijf maar op mijn lamp.....")
        Vraag5()

    elif vraag4 == "B" or vraag4 == "b":
        print("")
        print("Zozo jij hebt geduld :)")
        Vraag5()
        
    else:
        print("")
        print("Niks ingevuld")
        time.sleep(1)
        Vraag4()

def Vraag5():
    print("")
    vraag5 = input("Je kan onzichtbaar worden en teleporteren OF… gedachten van mensen lezen en vliegen, wat kies je? ")

    if vraag5 == "A" or vraag5 == "a":
        print("")
        print("Telepoorteren naar?!")
        Einde()

    elif vraag5 == "B" or vraag5 == "b":
        print("")
        print("Geen misbruik van maken he ")
        Einde()

    else:
        print("")
        print("Niks ingevuld")
        time.sleep(1)
        Vraag5()

def Einde():
    print
    print("")
    time.sleep(1)
    print("Dit is was mijn opdracht: Daily Choices. ")

          
Vraag1()


