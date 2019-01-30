'''
Flight Booking system
'''
import re


class BookTicket(object):
    # business class data
    bColumnCount = 2
    bRowCount = 1
    bNoOfSeatsPerCol = 4
    status = True

    bTotalSeats = bColumnCount * bRowCount * bNoOfSeatsPerCol
    bWindowSeats = bRowCount * 2
    bAisleSeats = (bColumnCount + bColumnCount - 2) * bRowCount
    bOthersSeats = bTotalSeats - (bWindowSeats + bAisleSeats)

    # Economy class data
    eColumnCount = 3
    eRowCount = 10
    eNoOfSeatsPerCol = 4

    eTotalSeats = eColumnCount * eRowCount * eNoOfSeatsPerCol
    eWindowSeats = eRowCount * 2
    eAisleSeats = (eColumnCount + eColumnCount - 2) * eRowCount
    eOthersSeats = eTotalSeats - eWindowSeats - eAisleSeats

    def bookTicket(self, fClass, preference):
        if re.search('business', fClass, re.IGNORECASE):
            if re.search('window', preference, re.IGNORECASE):
                if self.bWindowSeats > 0:
                    self.bWindowSeats -= 1
                    print self.bWindowSeats
                else:
                    self.status = False
            elif re.search('aisle', preference, re.IGNORECASE):
                if self.bAisleSeats > 0:
                    self.bAisleSeats -= 1
                else:
                    self.status = False
        elif re.search('economy', fClass, re.IGNORECASE):
            if re.search('window', preference, re.IGNORECASE):
                if self.eWindowSeats > 0:
                    self.eWindowSeats -= 1
                else:
                    self.status = False
            elif re.search('aisle', preference, re.IGNORECASE):
                if self.eAisleSeats > 0:
                    self.eAisleSeats -= 1
                else:
                    self.status = False
        return self.status


print "Welcome to Flight Booking System"

bookTicketObj = BookTicket()

while True:
    bookResponse = raw_input("Do you want ticket now ? ")
    if bookResponse.lower() == 'y' or bookResponse.lower() == 'yes':
        classResponse = raw_input("Select Business/Economy ? ")
        if classResponse.lower() == "business" or classResponse.lower() == 'economy':
            preferenceResponse = raw_input("Select Window/Aisle? ")
            if preferenceResponse.lower() == 'window' or preferenceResponse.lower() == 'aisle':
                pName = raw_input("Enter your Name: ")
                pAge = input("Enter your Age: ")
                if bookTicketObj.bookTicket(classResponse, preferenceResponse):
                    print "{}, your {}({}) ticket has booked.".format(pName, classResponse, preferenceResponse)
                else:
                    print "Sorry, No Ticket Available"
                    break
        else:
            print "Please enter valid class.."
            continue
    elif bookResponse.lower() == 'n' or bookResponse.lower() == 'no':
        print "Thank you for visiting..."
        break
    else:
        continue

