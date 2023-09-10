class Train:
    def __init__(self , name , fare , seats):
        self.name =  name
        self.fare =  fare
        self.seats = seats

    def getStatus(self):
        print("****************************************************")
        print(f"The name of the train is {self.name}")
        print(f"The seats availabel in this train is {self.seats}")
        print("****************************************************")

    def fareInfo(self):
        print(f"The price of the ticket is :{self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seat}  ")
            self.seats =  self.seays-1
        else:
            print("Sorry the train is full kindly try in tatkal")

    def cancleTicket(self):
        pass
    def cancleTicket(self):
        pass

intercity = Train("Intercity Exprss: 14015" ,90,300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()

