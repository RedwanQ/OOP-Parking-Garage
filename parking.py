

class Parking():


    price = 4.99
    
    

    # def __init__(self):
        # self.tickets = [1,2,3]
        # self.spaces = [1,2,3]
        # self.current_ticket = {}

    tickets = [1,2,3]
    spaces = [1,2,3]
    current_ticket = {}



    def take_ticket():
        take_ticket1 = input('Would you like to park here Y/N?').lower()

        if take_ticket1 == 'n':
            print('See you soon!')
        if take_ticket1 == 'y':
           Parking.current_ticket[Parking.tickets.pop()] = False
           print(Parking.current_ticket) 
        
        

    def payforparking():
        input('What is your ticket number')
        if Parking.current_ticket == {}:
            print('Please take a ticket!')
        else:
           pay = input(f'Please pay {Parking.price}')
        if pay == '4.99':
            Parking.tickets.append(Parking.current_ticket)

        



    def leave_garage():
        print(Parking.current_ticket)


def driver():
    while True:
        user = input('Do you want to: Park/Pay/Leave/Quit').lower()
        if user == 'park':
            Parking.take_ticket()
        if user == 'pay':
            Parking.payforparking()
        if user == 'leave':
            Parking.leave_garage()
        if user == 'quit':
            break
        else:
            print('Invaild Input')
            

driver()

# parking = Parking()
# parking.take_ticket() 
# parking.payforparking()      
            



        

      

    




    
