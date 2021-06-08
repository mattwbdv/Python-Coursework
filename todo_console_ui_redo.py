# Basic to-do application with user interaction happening in the console only

# Imports
from datetime import datetime
from datetime import date


# Data structure for todo items
items = ()
selection = "0"

# While loop to keep running the program
while selection != "5":
    if selection == "0":
        #  User instructions
        prompt0 = ('Main menu:')
        prompt1 = ('1)  List all incomplete todo items')
        prompt2 = ('2)  List incomplete todo items due today')
        prompt3 = ('3)  Add a todo item')
        prompt4 = ('4)  Complete a todo item')
        prompt5 = ('5)  Quit')
        print(prompt0, prompt1, prompt2, prompt3, prompt4, prompt5, sep='\n')

        # User selection for change
        selection = input('Enter your choice> ')

    # Listing incomplete todo items
    elif selection == "1":
        items_not_done = []
        for x in range(0, len(items)):
            if items[x] is False:
                items_not_done.append(items[x+1])
        print(items_not_done)
        selection = "0"

    # Listing incomplete todo items due today
    elif selection == "2":
        due_today = []
        for x in range(0, len(items)):
            if items[x] is False:
                if items[x+2].date() == date.today():
                    due_today.append(items[x+1])
        print(due_today)
        selection = "0"

    # Adding a todo item
    elif selection == "3":
        newItemDescription = input('Enter item description: ')
        newItemDueDate = input('Enter due date/time (MM/DD/YYYY hh:mm): ')
        newItemDueDate = datetime.strptime(newItemDueDate, '%m/%d/%Y %H:%M')

        print(newItemDueDate)
        items = items + (False, newItemDescription, newItemDueDate)
        selection = "0"

    # Complete a todo item
    elif selection == "4":
        print('Incomplete items: ')
        for x in range(0, len(items)):
            if items[x] is False:
                print(x, ') ', items[x+1], items[x+2])

        itemDone = input('Enter item to complete: ')
        itemToDelete = int(itemDone)
        items[itemToDelete] = True
        selection = "0"
