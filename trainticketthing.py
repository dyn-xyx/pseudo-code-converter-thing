goingTimes =     [9,11,13,15]
gn_ticketCount = [480,480,480,480]
gn_money =       [0.0,0.0,0.0,0.0]

returningTimes = [10,12,14,16]
rt_ticketCount = [480,480,480,640]
rt_money =       [0.0,0.0,0.0,0.0]


working = 1
arrivalStart = 0
journeyTkPrice = 0.0
discountPrice = 0.0

while(working != 0):
    print("Departing \t\t      Tickets Available \t\t\t    Arriving \t\t\t\t Tickets Available")
    for i in range(4):
        print(goingTimes[i],"\t\t\t\t\t", gn_ticketCount[i],"\t\t\t\t\t", returningTimes[i],"\t\t\t\t", rt_ticketCount[i])

    
    goingInput = int(input("\nEnter your departing hour: "))
    while goingInput not in goingTimes:
        print("Kindly choose an hour from: ", goingTimes)
        goingInput = int(input("Enter your departing hour: "))
    
    
    for index in range(4):
        if(goingTimes[index] == goingInput):
                arrivalStart = index        
    
    print("\nArriving hours available: ")
    for index in range(arrivalStart, 4):
        print(returningTimes[index])
    
    
    rtrnInput = int(input("\nEnter your arrival hour : "))
    while rtrnInput not in returningTimes:
        print("You have selected an invalid returning hour!")
        rtrnInput = int(input("Enter your arrival hour : "))

    
    for index in range(4):
        if(returningTimes[index] == rtrnInput):
            returnStart = index     

    psngrCount = int(input("Enter the passengers count (max group of 80 allowed): "))
    while (psngrCount<1 or psngrCount>80):
        print("Kindly enter a passenger count between 1 to 80.")
        psngrCount = int(input("Enter the passengers count (max group of 80 allowed): "))

    while(psngrCount > gn_ticketCount[arrivalStart] or psngrCount > rt_ticketCount[returnStart]):
        print("There are only ",gn_ticketCount[arrivalStart],"tickets available!")
        psngrCount = int(input("Enter an appropriate passengers count: "))


    gn_ticketCount[arrivalStart] = gn_ticketCount[arrivalStart] - psngrCount
    rt_ticketCount[returnStart] = rt_ticketCount[returnStart] - psngrCount
    
    if(psngrCount>=10):
        freeCount = int(psngrCount / 10)
        journeyTkPrice = (25*(psngrCount-freeCount))
        print("Congratulations! The cost of ", freeCount," tickets has been waived!")

    else:
        journeyTkPrice =  25*psngrCount

    print("\nTotal Ticket Price for two-way journey is: $",2*journeyTkPrice)

    gn_money[arrivalStart] = gn_money[arrivalStart] + journeyTkPrice
    rt_money[returnStart] = rt_money[returnStart] + journeyTkPrice
    
    
    working = int(input("\nEnter 0 to call it a day and see stats or 1 to continue: \n"))

    print("\n-----------------------------------------------------------------------------------------------------\n")


print("Individual Journey Statistics: ")
print("Journey \t\t Tickets Sold \t\t\t                Total Cost")


for index in range(4):
    gn_ticketCount[index] = 480 - gn_ticketCount[index]
    
for index in range(3):
    rt_ticketCount[index] = 480 - rt_ticketCount[index]

rt_ticketCount[3] = 640 - rt_ticketCount[3]

for index in range(4):
    print(goingTimes[index], "\t\t\t\t", gn_ticketCount[index],"\t\t\t\t\t $", gn_money[index])
    print(returningTimes[index], "\t\t\t\t", rt_ticketCount[index],"\t\t\t\t\t $", rt_money[index])


arrPassengers = 0
retPassengers = 0
arrTotal = 0.0
retTotal = 0.0

for index in range(4):
    arrPassengers = gn_ticketCount[index] + arrPassengers
    retPassengers = rt_ticketCount[index] + retPassengers

    arrTotal = arrTotal + gn_money[index]
    retTotal = retTotal + rt_money[index]

maxGoingTickets = gn_ticketCount[0]
maxRetTickets = rt_ticketCount[0]
maxGoingTicketsIndx= 0
maxRetTicketsIndx = 0

for index in range(4):
    if(gn_ticketCount[index] > maxGoingTickets):
        maxGoingTickets = gn_ticketCount[index]
        maxGoingTicketsIndx = index

    if(rt_ticketCount[index] > maxRetTickets):
        maxRetTickets = rt_ticketCount[index]
        maxRetTicketsIndx = index

    
print("-----------------------------------------------------------------------------------------------------\n")
print("Complete Day Statistics")
print("\nTotal Passengers count: ",arrPassengers+retPassengers)
print("Total Tickets Sold value: $",arrTotal+retTotal)


if(gn_ticketCount[maxGoingTicketsIndx] > rt_ticketCount[maxRetTicketsIndx]):
    print("Train with maximum passengers was of the Hour: ",goingTimes[maxGoingTicketsIndx])

elif(gn_ticketCount[maxGoingTicketsIndx] < rt_ticketCount[maxRetTicketsIndx]):
    print("Train with maximum passengers was of the Hour: ",returningTimes[maxRetTicketsIndx])