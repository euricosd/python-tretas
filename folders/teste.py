import os
 
##path = os.path.join("C:\\","temp")

path = str(input("Your path, please:\n"))

while True:
    if path == 'q':
        break
    elif os.path.exists(path):
        print(path + ' : exists')
        if os.path.isdir(path):
            print(path + ' : is a directory')
        else:
            print(path, ': is *not* a directory')
    else:
        print(path, ': does *not* exist')

    path = str(input("\nYour path, please (q to quit):\n"))
