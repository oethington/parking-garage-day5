# parking garage class
# ticket list to keep track of tickets
# count of how many spaces are available increase and decrease as people leave

# what action exit/enter

# enter
# generate ticket # - based on ticket count
# print here is the total, enjoy your stay
# return to what action
# decrease space/ticket count by 1
# store user info in dict

# exit
# ticket#
# print here is your total:$$$ pay now? Y/N
# return to what action
# increase space/ticket count by 1
# remove user from storage
            



text = {
    'enter' : 'Enjoy your stay! Your ticket number is {ticket} ',
    'task_query' : 'Would you like to enter or exit the garage?: ',
    'exit' : 'Here is your total: {price}, Pay Now?',
    'full' : "Sorry the garage is full. Try again later",
    'ticketUse' : 'Number of available  tickets: ',
    'availableSpace' : 'Number of available spaces: ',
    'revenue' : 'Current revenue: '
}

class Garage():
    def __init__(self, price):
        self.tickets = 0
        self.spaces = 5
        self.price = price
        self.parkingSpaces = []
        self.ticket_count = 5
        self.currentTicket = {}
    def storedData(self, newTicket):
        self.currentTicket.append({
            'ticket': self.ticket
        })
    def show(self):
        print(text['ticketUse'], self.ticket_count, ':', text['availableSpace'], self.spaces)

    def enterGarage(self):
        if len(self.currentTicket) > self.ticket_count:
            print(text['full'])
        else:
            
            print('This is your parking space')
            self.currentTicket['paid'] = False
            self.tickets += 1
            print(self.tickets)
            self.decrease_ticket()
            self.decrease_space()
    def decrease_ticket(self):
        self.ticket_count -= 1
    def decrease_space(self):
        self.spaces -= 1
    def exitGarage(self):
        payment_paid = input('please pay $6')
        if payment_paid == '$6':
            print('ticket has been paid and you have 15mins to leave.')
            print('Thank you have a nice day!')
        self.currentTicket['paid'] = True
        self.increase_ticket()
        self.increase_space()
    def increase_ticket(self):
        self.ticket_count += 1
    def increase_space(self):
        self.spaces += 1
    def main(self):
        while True: 
            enter_or_exit = input(text['task_query'])
            if enter_or_exit  == 'enter':
                self.enterGarage()
            elif enter_or_exit == 'exit':
                self.exitGarage() 
            elif enter_or_exit == 'admin':
                self.show()
                break

badassGarage = Garage(6)
badassGarage.main()
