import os.path
import time

file_path = 'me.txt'

while not os.path.exists(file_path):
    time.sleep(1)
    
if os.path.isfile(file_path):
    print("hupp")
    fob=open(file_path,'r');
        read=fob.readlines();
        for i in read:
            print i
else:
    print("hepp")
#    raise ValueError("%s isn't a file!" % file_path)