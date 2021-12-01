# One.py
# Built-in Variable
# __name__

def func():
    print('func() in one.py')


# The function is to make python script more manageable, splitting between 1)Function, class 2) Run program
if __name__ == '__main__':
    print('One.py is being run directly!')
else:
    # print('One.py has been imported!')
    pass
