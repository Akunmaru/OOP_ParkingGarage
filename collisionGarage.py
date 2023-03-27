# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 


# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# By the end of this project each student should be able to:
# - Explain and/or demonstrate creating classes
# - Explain and/or demonstrate creating class methods
# - Explain and/or demonstrate class instantiation

class Garage():
    def __init__(self, spaces, tickets):
        self.spaces = spaces    
        self.tickets = tickets
        self.parking_ticket = {"paid" : False}
    
    def takenTicket(self):
        self.tickets -= 1
        self.spaces -= 1
    
    def payForParking(self):
        print('\n\n\nYou owe us: $600\n')
        while True:
            paying = input('Enter payment amount to confirm\n$')
            try:
                int(paying)
                # while True:
                if int(paying) > 600:
                    change = int(paying) - 600
                    print(f'\n\nYour ticket is paid!\nHere is your change ${change}\nYou have 15 minutes to leave!')
                    self.parking_ticket.update({"paid" : True})
                    break
                elif int(paying) == 600:
                    print('\n\nYour ticket is paid!\nYou have 15 minutes to leave!')
                    self.parking_ticket.update({"paid" : True})
                    break
                elif paying == '':
                    print('You have not paid \n You have 15 minutes...I betta get my money when you come back')
                else:
                    print('Insufficient funds...you broke')
            except:
                print('Use digits...')
    
    def leave(self):
        if self.parking_ticket == {"paid": True}:
            print("Thank you!! Have a lovely day!")
            self.spaces += 1
            self.tickets += 1
        else:
            print('\n\n\nYou owe us: $600\n')
        while True:
            paying = input('Enter payment amount to confirm\n$')
            try:
                int(paying)
                # while True:
                if int(paying) > 600:
                    change = int(paying) - 600
                    print(f'\n\nYour ticket is paid!\nHere is your change ${change}\nYou can go now...')
                    self.spaces += 1
                    self.tickets += 1
                    break
                elif int(paying) == 600:
                    print('\n\nYour ticket is paid!\nYou can go now...')
                    self.spaces += 1
                    self.tickets += 1
                    break
                elif paying == '':
                    print('IM NOT PLAYING ANYMORE GAMES GIVE ME MY MONEY THEN YOU CAN LEAVE!!!!')
                else:
                    print('Insufficient funds...you broke')
                break
            except:
                print('Use digits...')

    def showSpace(self):
        print(f"Remaining parking spots: {self.spaces}")
        

collisionGarage = Garage(10,10)

def initialize():
    while True:
        spoken = input('\nWelcome to Collision Garage!\nHave you already parked a car here? (enter "yes" or "no")')
        if spoken.lower() == 'no':
            jackal = input('Would you like to park here? (enter "yes" or "no")') 
            if jackal.lower() == 'yes':
                collisionGarage.takenTicket()
                collisionGarage.payForParking()
            elif jackal.lower() == 'no':
                print("We didn't want your slow, dirty, ugly car in here anyways")
                break
        elif spoken.lower() == 'yes':
            collisionGarage.leave()
        else:
            print('Try another command')

initialize()
