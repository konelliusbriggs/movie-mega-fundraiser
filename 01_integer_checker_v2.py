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

age_error = "Please enter an age between 12 and 130"
age = int_check("Age: ", age_error)

