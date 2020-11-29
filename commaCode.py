# Write a function that takes a list value an argument and returns a string with all the items separated by a
# comma and space, with and inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu and cats'. But your function should be able to work with any
# list value passed to it.

# spam = ['apples', 'bananas', 'tofu', 'cats']

someList = []   # Empty list
while True:     # while True trigger the following:
    print('Enter the ' + str(len(someList) + 1) + '. item for your grocery list. ' + '(Or enter nothing to stop):')
    # str(len(someList) + 1) will add plus one for each loop
    item = input()  # Enter your items
    if item == '':  # If no input was made break will stop the loop.
        break
    someList = someList + [item]   # list concatenation
print('Your grocery list for today contains:')  # Simple text print for the result
print(', '.join(someList[:-1]) + ' and ' + someList[-1])
# This prints out the items in someList after the loop is complete and separates them with a comma.
# Using :-1 will display all the items besides the last item in the list. -1 Will return just the last item.


