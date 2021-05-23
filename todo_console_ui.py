# Basic to-do application with user interaction happening in the console only 

# Imports 
from datetime import datetime
from datetime import date

# Data structure for todo items 
items = []
dueDates = []
status = []
selection = '0'

# While loop to keep running the program 
while selection != 5:
    if selection == '0':
        #  User instructions
        prompt0 = ('Main menu:')
        prompt1 = ('1)  List all incomplete todo items')
        prompt2 = ('2)  List incomplete todo items due today')
        prompt3 = ('3)  Add a todo item')
        prompt4 = ('4)  Complete a todo item')
        prompt5 = ('5)  Quit')
        print(prompt0, prompt1, prompt2, prompt3, prompt4, prompt5, sep = '\n')

        # User selection for change 
        selection = input('Enter your choice> ')

    # Listing incomplete todo items 
    elif selection == '1':
        for x in range(0, len(items)):
            if status[x] == 'Y':
                print(items[x])
        selection = '0'

    # Listing incomplete todo items due today
    elif selection == '2':
        for x in range(0, len(items)):
            dateToday = date.today()
            dateToTest = dueDates[x].date()
            status = status[x]
            if dateToTest == dateToday and status == 'Y':
                print(items[x], dueDates[x])
        selection = '0'


    # Adding a todo item 

    elif selection == '3':
        newItemDescription = input('Enter item description: ')
        newItemDueDate = input('Enter due date/time (MM/DD/YYYY hh:mm): ')
        newItemDueDate = datetime.strptime(newItemDueDate, '%m/%d/%Y %H:%M')

        print(newItemDueDate)
        items.append(newItemDescription)
        dueDates.append(newItemDueDate)
        status.append('Y')
        selection = '0'

    # Complete a todo item 
    elif selection == '4':
        print('Incomplete items: ')
        for x in range(0, len(items)):
            if status[x] == 'Y':
                print(x, ') ', items[x], dueDates[x])

        itemToDelete = input('Enter item to complete: ')
        itemToDelete = int(itemToDelete)
        status[itemToDelete].replace("Y", "N") 
        selection = '0'

