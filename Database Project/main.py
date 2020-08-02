from queryDatabase import *



inLoop=1
print("Welcome to the Bus Inquiry portal")
print("Choose one of the available options")
while inLoop:

    print("1. Find buses between two cities")
    print("2. Get bus details")
    print("3. Get bus route details")
    print("4. To exit")
    choice=input("Enter your choice : ")
    if choice == "1":
        source=input("Enter your query Source : ").upper()
        destination= input("Enter you destination : ").upper()
        getBusBwStations(source,destination)
        print("Press 1 to enquire more, any other key to exit")
        x = input()
        if x == "1":
            print("Make a choice")
        else:
            inLoop = 0

    elif choice == "2":
        busNo=input("Enter the bus no. to get its details : ").upper()
        getBusDetails(busNo)
        print("Press 1 to enquire more, any other key to exit")
        x=input()
        if x=="1":
            print("Make a choice")
        else:
            inLoop=0

    elif choice == "3" :
        a=input("Enter the bus number : ").upper()
        b=input("Enter the bus origin station  : ").upper()
        getBusRoute(a,b)
        print("Press 1 to enquire more, any other key to exit")
        x = input()
        if x == "1":
            print("Make a choice")
        else:
            inLoop = 0

    elif choice=="4":
        inLoop=0
        print("Thanks for choosing our service.")

    else:
        print("You made a wrong attemt. Please retry : ")



