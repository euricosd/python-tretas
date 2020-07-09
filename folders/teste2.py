import os

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  
dir = os.path.join("C:\\","Users","Filho Lindo", "dirs")
os.chdir(dir)

for i in abc:
    os.mkdir(i)
    os.chdir(i)
    print('Folder "' + i + '" is done and checked out') 

