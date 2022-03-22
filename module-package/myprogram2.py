# Built-in variable
# __name__ 

def myfunc():
    print('Hello World')

# Python do this on background, like main program, if run directly masuk ke if, kalau imported masuk ke else, 
# __name__ tidak sama dengan __main__, not run the function ketika mengetik import
if __name__ == '__main__':
    # RUN THE SCRIPT, KINDA LIKE MAIN PROGRAM, ORGANIZED FOR LARGER PYTHON PROGRAM, ESPECIALLY WHEN WORK WITH MODULE AND PACKAGE
    myfunc()
else:
    print('Imported')



