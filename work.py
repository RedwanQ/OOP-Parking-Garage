class Parking():

    price = 4.99
    curren_ticket = []
    parking_spaces = {}

    def __init__(self,tickets,spaces):
        self.tickets = tickets
        self.spaces = spaces
        pass


    def pay_forparking(self):
        pay_mom = input('Welcome do you want to park Y/N!')
        while pay_mom == 'Y':
            continue
        
        pay_me = input('Please pay $4.99 for your ticket!')
        if pay_me == '4.99':
            return('Have a good day')
        else:
            return('Please pay your ticket')
            pass

    def take_ticket(self):
        pass


    def leave_garage(self):
        pass

    def driver_input():
        pass

    




    
