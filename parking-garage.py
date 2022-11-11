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
    'enter' : "Enjoy your stay! Your ticket number is {ticket}",
    'task_query' : 'Would you like to enter or exit the garage?: ',
    'exit' : 'Here is your total: {price}, Pay Now?',

}

ticket = [1, 2, 3, 4, 5]

parkingSpaces = [1, 2, 3, 4, 5]

currentTicket = {}

class Garage():
    def storedData(newTicket):
        currentTicket.append({
            'currentTicket': ticket
        })

    def enterGarage():
        

    def exitGarage():
        pass

    def parkingCount():
        pass

    def main():
        while True:
            choice = input(text['task_query'])
            choice = input(text['enter'])
            storedData(currentTicket)
            choice = input(text['exit'])

            while True:
                

    main()


