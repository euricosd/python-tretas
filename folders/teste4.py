import os
import random
import string
from pathlib import Path

def get_random_string():
    global result_str
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(0, 30))
    return result_str

def get_random_long():
    global long_str
    letters = string.ascii_letters
    long_str = ''.join(random.choice(letters) for i in range(0, 50)) + " \\\\"
    for z in range (0, 19):
        long_str += "\n" + ''.join(random.choice(letters) for i in range(0, 50)) + " \\\\"
    return long_str

dir = os.path.join("C:\\","Users","Filho Lindo", "dirs")
os.chdir(dir)

for i in range(0, 100):
    get_random_string()
    os.mkdir(result_str)
    os.chdir(result_str)
    for a in range (0, 50):
        get_random_string()
        os.mkdir(result_str)
        os.chdir(result_str)
        for b in range(0, 10):
            get_random_string()
            get_random_long()
            f = open(os.path.join(os.getcwd(), str(result_str + ".txt")), "x")
            f.write(long_str)
            f.close()
        parentb = os.path.dirname(os.getcwd())
        os.chdir(parentb)

    print(str(i + 1) + "%")
                        
    os.chdir(dir)
##    os.chdir(str(randa))
##    for y in range(0, 30):
##        randb = randint(100000000, 999999999)
##        os.mkdir(i)

