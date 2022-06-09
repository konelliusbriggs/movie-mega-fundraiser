# import statement...
import re 
import pandas

# functions go here...

# Checks that the ticket name is not blank...
def not_blank(question, error_message):
    valid = False 

    while not valid: 
        response = input(question)

        if response != "":
            return response 
        else: 
            print(error_message)

# Checks for a integer more than 0...
def int_check(question): 
  
  error = "Please enter a whole number between 12 and 130"

  valid = False 
  while not valid:

    try:
      response = int(input(question))

      if response <= 0:
        print(error)
      else:
        return response

    except ValueError:
      print(error)

# Checks number of tickets left and warns user
# If the maximum has been aproached 
def check_tickets(tickets_sold, ticket_limit):
    # Tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1: 
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))
        print()
    # Warns the user that there is only one seat left.
    else:
        print("You only have one available seat left.")
        print()
    # Returns the statement
    return ""

# Tickets prices based off their ages
def get_ticket_price():

    # Gets age between 12 and 120
    age = int_check("What is your age?: ")
    print()

    # Checks that age is valid...
    if age < 12:
        print("Sorry you are too young for this movie")
        return "Invalid Ticket Price"
    elif age > 120:
        print("That is very old - this must be a mistake on your part")
        return "Invalid Ticket Price"

    if 12 <= age < 16:
        ticket_price = 7.5
    elif 16<= age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price
    
# Checks to see the users valid responses to the questions that are asked
# if not valid , shows error message
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full item
        if choice in var_list:

            # Get full name of snack 

            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # If the options are not valid - set not_valid to no 
        else:
            is_valid = "no"

    # if the snack os not Ok - ask question again 

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

# Get's the list of snacks 
def get_snack():

    # Regular expression to find if item starts with a number 
    number_regex = "^[1-9]"

    # Valid snacks holds list of all snacks, each item in valid snacks is a list with valid options fo each snack <full name, letter code (a-e)
    # and possible abbreviations etc
    valid_snacks = [
    ["popcorn", "p", "pop", "corn", "a"],
    ["M&Ms", "M&M", "m&m", "mms", "mm", "m", "b"],
    ["pita Chips", "chips", "pc", "pita", "c"],
    ["water", "w", "h20" "d"],
    ["orange juice", "oj", "o", "juice", "orange", "e"]
    ]

    # holds the snack order 
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

        snack_row = []

        # Asks user for desired snack and put it in lower case 
        desired_snack = input("What snack(s) would you like?: ").lower()
        print()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number , seperate it into two different numbers 
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
    
        else:
            amount = 1
            desired_snack = desired_snack

        # Remove the spaces before and after the snack
        desired_snack = desired_snack.strip()

        # Checks if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # Checks snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        snack_row.append(amount)
        snack_row.append(snack_choice)
            
        # Add snack and amount to list 
        amount_snack = "{} {}".format(amount, snack_choice)

        # checks that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)

# Currency formatting function...
def currency(x):
    return "${:.2f}".format(x)

# Functions to show instructions if needed...
def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions?: ")

        show_help = string_check(show_help, options)

        if show_help == "invalid choice":
            print("Please enter yes / no")

    if show_help == "Yes":
        print()
        print("** Mega Movie Fundraiser Instructions **")
        print()
        print("You are selling Movie Tickets for the people that decided to join you for your rowing club funding")
        print("You have found a 150 seat theater that you have rented out for this special occasion")
        print("You have to make sure that you do not exceed this limit, for risk that you may get kicked out")
        print("You created this program so you could see how many atendees you have")
        print("They can submit their:")
        print("· Name ")
        print("· Age ")
        print("· And whatever snacks they would like (preorder their own snacks) ")
        print("So make sure this makes it easier for you and have fun")
        print()
    return ""

# Main routine starts here...

# Setup dictionaries / lists needed to hold the data

# the list for valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# the lists for valid surcharge responses
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# initialise loop so that it runs atleast once 
MAX_TICKETS = 5 

name = ""
ticket_count = 0 
ticket_sales = 0

# Initialize list (to make data-frame in due course)
all_names = []
all_tickets = []

# Snacks Lists...
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# store surcharge multiplier
surcharge_mult_list = []

# xx summary data...
summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water", "Orange Juice",
"Snack Profit", "Ticket Profit", "Total Profit"]

summary_data = []

# Data frame dictionaries 
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn':popcorn,
    'Water':water,
    'Pita Chips':pita_chips,
    'M&Ms':mms,
    'Orange Juice':orange_juice,
    'Surcharge Multiplier': surcharge_mult_list
}

# Summary Dictionary...
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# Cost of each snack...
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}


# Ask the user if they have used the program before & show instructions..
instructions(yes_no)

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # Checks to see if the limit has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

    # Get name (cannot be blank)
    name = not_blank("Could i please get your name?: ", "sorry - name cannot be blank")

    # End the loop if the exit code is typed
    if name == "xxx":
        break

    # Get ticket price based off their age 
    ticket_price = get_ticket_price()

    print("Ticket Price", ticket_price)

    # If the age is invalid - restart the loop (and get the name again)
    if ticket_price == "Invalid Ticket Price":
        continue

    ticket_count += 1 
    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks 
    # ask the user if they want a snack
    
    snack_order = get_snack()

    # Assume no snacks have been brought...
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1]=amount

    # Ask for the payment method... 
    how_pay = "Invalid Choice"
    while how_pay == "Invalid Choice":
        how_pay = input("Please choose a payment method first (Cash or card): ").lower()
        how_pay = string_check(how_pay, pay_method)

    # working credit or cash 
    if how_pay == "Credit":
        surcharge_multiplier = 0.05 
    else:
        surcharge_multiplier = 0
    
    surcharge_mult_list.append(surcharge_multiplier)

# End of tickets / snacks / payment loop...

# Create dataframe and set index to name collumn
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# Create collumn called 'Sub-Total'
# Fill it prace for snacks and tickets
movie_frame["Snacks"] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice'] 

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

# Surcharge collumn
movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge Multiplier"]

# Total column
movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# Shorten collumn names...
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
 'Pita Chips': 'Chips', 'Surcharge Multiplier': 'SM'})

# Setup summary dataframe
# populate snack items...
for item in snack_lists:
    # Sum items in each snack list...
    summary_data.append(sum(item))

# Get snack profit 
# Get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2

# Calculate ticket profit...
ticket_profit = ticket_sales - (5 * ticket_count)

# Work out total profit and add to list...
total_profit = snack_profit + ticket_profit 

# Format dollar amounts and add to lists...
dollar_amounts = [snack_profit, ticket_profit, total_profit]
for item in dollar_amounts:
    item = "{:.2f}".format(item)
    summary_data.append(item)

# Create summary frame...
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# Setup Columns to be printed..
pandas.set_option('display.max_columns', None)

# ** Pre-Printing / Export **
# Format currency values so they have $'s

# Ticket details Formatting (uses currency function)
add_dollars = ['Ticket', 'Snacks', 'Surcharge', 'Total', 'Sub Total']
for item in add_dollars:
    movie_frame[item] = movie_frame[item].apply(currency)

# Write each frame to a seperate csv files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")


print() 

# Abbreviatied summary frame
print()
print("*** Ticket / Snack information ***")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total', 'Surcharge', 'Total']])

print()

print("*** Snack / Profit Summary ***")
print()
print(summary_frame)

# Print all statements
print_all = input("Print all columns?? (y) for yes ")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total', 'Surcharge', 'Total']])

print()

# Tells users if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
   