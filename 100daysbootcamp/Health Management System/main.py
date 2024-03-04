import datetime

def gettime():
    '''this function gives the current datetime'''
    return datetime.datetime.now()


name_list = []

def put_info():
    '''this function put the information to the local file'''
    name = str(input("Enter your name: "))
    if not name in name_list:
        name_list.append(name)
        food_exe = int(input("Enter 1 for food and 2 for exercise: "))
        write = str(input("Write Here: "))
        with open(f'{name}-{food_exe}.txt', 'a') as op:
            op.write(str(str(gettime()) + ':' + write + '\n'))
            print("Successfully Written")
            
def get_info():
    '''this function get the information from the local file'''
    get_name = str(input("Enter the name to get Data: "))
    get_item = int(input("Enter 1 for food and 2 for Exercise: "))
    file =open(f"{get_name}-{get_item}.txt")
    for i in file:
        print('\n')
        print(i, end='')
        print('\n')
        


query = int(input("Enter 1 for storing info. 2 for retrieving info."))
if query==1:
    put_info()
else:
    get_info()