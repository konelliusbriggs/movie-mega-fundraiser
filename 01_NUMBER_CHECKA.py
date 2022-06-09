def int_check(question, low_num, high_num):

    error= "please enter a whole number between {} and {}".format(low_num, high_num)


    valid = False
    while not valid:
        

        # ask user for number and check it is valid
        try:
            response = int (input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)


        # if an integer is not entered, display and error
        except ValueError:
            print(error)

age = int_check("Age: ", 12, 130)






# initialise variables
snack_ok = ""
snack = ""



#loop three times to make testing quicker
for item in range(0' 3):
    
    # ask user for desired snack amd put it in lowercase
    desired_snack = input("snack: ").lower()

    for var_list in valid_snacks:
        # if the snacks is in one of the lsits, return the full 
        if desired_snack in var_list:

            #get full name of snack and put it 
            #in title case so it looks nice when outputted
            snack = var_list[0].title()
            snack_ok = "yes"
            break

        #if the chosen snackis not valid, set snack_ok to no
        else:
            snack_ok = "no"