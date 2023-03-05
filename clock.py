#!/usr/bin/python3
#*******Python时间程序*******
import time
import os
from itertools import repeat 
os.system("color 02")
for _ in repeat(None): # Other operations.
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    str = "当前时间:" + time.asctime(t)
    print(str);
    os.system('clear')
#*******C++时间程序*******
#    #include<bits/stdc++.h>
#using namespace std; 
#int main(void) 

#{ 

#for(;;){
#//获取系统时间 

#time_t now_time=time(NULL); 

#//获取本地时间 

#tm* t_tm = localtime(&now_time); 

#//转换为年月日星期时分秒结果，如图： 

#printf("当前时间 : %s\n", asctime(t_tm)); 

#//将时间转换为秒 

#time_t mk_time = mktime(t_tm); 

#//也可以自己定义一个时间 

#//定义截止时间 

#struct tm deadline_tm; 

#deadline_tm.tm_sec=0;//[0~59] 

#deadline_tm.tm_min=10;//[0~59] 

#deadline_tm.tm_hour=13;//[0~23] 

#deadline_tm.tm_isdst=0;//default 

#deadline_tm.tm_mday=31;//[1~31] 
#deadline_tm.tm_mon=2;//[0~11] 
#system("clear");
#}
#return 0;
#}