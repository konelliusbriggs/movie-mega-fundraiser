# start of loop

#initilise loop so that it runs at least once 
name = "" 
count = 0 
MAX_TICKETS = 5 

while name != "xxx" and count < MAX_TICKETS:
    print("you have {} seats " 
          "left".format(MAX_TICKETS - count))

    # get details
    name = input ("name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("you have sold all the available tickets!")
else:
    print("you have sold {} tickets. /n"
    "there are {} places still avalible"
    .format (count, MAX_TICKETS - count))
