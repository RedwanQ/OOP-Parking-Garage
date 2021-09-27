# Redwan

class Parking():


    price = 4.99
    tickets = [1,2,3]
    spaces = [1,2,3]
    current_ticket = {}



    def take_ticket():
        ticket = input('Would you like to a ticket Y/N? ').lower()

        if ticket == 'n':
            print('See you soon!')
        if ticket == 'y':
           Parking.current_ticket[Parking.tickets.pop()] = False
           print(Parking.current_ticket) 
        
        

    def payforparking():
        input('What is your ticket number? ')
        if Parking.current_ticket == {}:
            print('Please take a ticket!')
            Parking.take_ticket()
        else:
           pay = input(f'Please pay {Parking.price}. ')
           Parking.current_ticket = True
           print(Parking.current_ticket)
        
   

        
    def leave_garage():
        if Parking.current_ticket == True:
            print('Thank you have a good day!')
        elif Parking.current_ticket == {}:
            print('Please go get a ticket!')
            Parking.take_ticket()
        elif Parking.current_ticket is not {}:
            print('Please pay your parking fee before existing. ')
            print(Parking.current_ticket)
     
        
        

def driver():
    while True:
        user = input('Do you want to: Park/Pay/Leave/Quit ').lower()
        if user == 'park':
            Parking.take_ticket()
        elif user == 'pay':
            Parking.payforparking()
        elif user == 'leave':
            Parking.leave_garage()
        elif user == 'quit':
            break
        else:
            print("Invalid response please try again.")
        
            
            

driver()
# Redwan

            



        

      

    




    
