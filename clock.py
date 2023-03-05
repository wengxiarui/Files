#!/usr/bin/python3
#*******Python时间程序*******
import time
import os
from itertools 
import repeat 
for _ in repeat(None): # Other operations.
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    str = "当前时间:" + time.asctime(t)
    print(str);
    os.system('cls')
