# import statements


# functions goes here

# checks user enters something (ie: blank response not allowed)
def not_blank(question, error_message):
    valid = False 

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)
# checks for an integer 
def int_check(question, error):

    valid = False
    while not valid:
        

        # ask user for number and check it is valid
        try:
            response = int (input(question))

            return response


        # if an integer is not entered, display and error
        except ValueError:
            print(error)


# main routine goes here

#set up dictionaries / lists needed to hold data 

#ask user if they have used the program before and show instructions if nessacery

# loop to get ticket details
#initilise loop so that it runs at least once 

name = "" 
count = 0 
MAX_TICKETS = 5 

while name != "xxx" and count < MAX_TICKETS:

    # get details

    name = not_blank("Name: ", "something went wrong")
    if name == "xxx":
        break

    age_error = "Please enter an age between 12 and 130"
    age = int_check("Age: ", age_error)

    if age < 12 or age > 130:
        print(age_error)
        continue

    # if age and name are OK - increase count
    count += 1
    
    # tells user how many seats are left 
    if count < 4:
        print("you have {} seats "
              "left".format(MAX_TICKETS - count))

    # warns user that only one seat is left!
    else:
        print("*** there is ONE seat left!! ***")
   

if count == MAX_TICKETS:
    print("you have sold all the available tickets!")
else:
    print("you have sold {} tickets. \n"
    "there are {} places still avalible"
    .format (count, MAX_TICKETS - count))


    # get name

    # get age (between 12 and 130)
    # 
    # calculate ticket price 
    # 
    # loop to ask for snacks
    # 
    # calculate snack price
    # 
    # ask for payment method (and apply subcharge if necesary)

# calculate total sales and profit
# output data to text file