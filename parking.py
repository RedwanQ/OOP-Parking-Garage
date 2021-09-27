# MAIN CLASS

class Parking():


    price = 4.99
    
    

    def __init__(self):
        self.tickets = [1,2,3]
        self.spaces = [1,2,3]
        self.current_ticket = {}



    def take_ticket(self):
        take_ticket = input('Would you like to park here Y/N?').lower()

        if take_ticket == 'n':
            print('Cya around')
        if take_ticket == 'y':
           self.current_ticket[self.tickets.pop()] = False
           print(self.current_ticket) 
        else:
            print('Invalid input')
        


    def payforparking(self,price):
       pay = int(input('What ticket do you have?'))
       pass

        
   


    def leave_garage(self):
        pass


parking = Parking()
parking.take_ticket()       
            



        

      

    




    
